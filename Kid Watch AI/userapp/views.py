from ast import Return
# from ssl import _PasswordType
from django.db.models import Avg,Max,Min,Sum,Count,StdDev,Variance
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from adminapp.models import *
from mainapp.models import *
from userapp.models import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from ytksa import settings
import requests
from django.utils.dateparse import parse_duration
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from django.core.paginator import Paginator
from langdetect import detect
from userapp.urdu_sentiment import get_urdu_sentiment
from django.core.paginator import Paginator

# Create your views here.

def main_user_login(request):
    if request.method == "POST":
        username=request.POST.get("email")
        password=request.POST.get("password")
        

        try:
            # s1=UserModel.objects.filter(user_status="accepted") | UserModel.objects.filter(user_status="warned")
            auth = UserdetailsModel.objects.get(user_email=username,user_password=password)
            if auth.user_status  == "accepted":
                request.session['user_id'] = auth.user_id
                messages.success(request,'Successfully Logged In')
                return redirect('user_index')
            elif auth.user_status == "pending":
                messages.info(request,'Your id is pending for registration ')
                return redirect('main_user_login')
            elif auth.user_status == "blocked":
                messages.error(request,'You Are BLOCKED From Logging In ')
                return redirect('main_user_login')
            else:
                messages.error(request,'You are not registered,try again after signup')
                return redirect('main_user_login')
            
        except:
            messages.error(request,'invalid login credentials')
            return redirect('main_user_login')
    return render(request,"main/main-user-login.html")




def user_index(request):
    user_id = request.session['user_id']
    auth = UserdetailsModel.objects.get(user_id = user_id)
    
    
    if request.method == 'POST':

        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        # comments_thread_url =' https://www.googleapis.com/youtube/v3/commentThreads' 
        s = request.POST['search']
        search_params = {
            'part': 'snippet',
            'q' : s,
            'key' : settings.GOOGLE_API,
            'maxResults':1,
            'type': 'comments'
        }

        req = requests.get(search_url, params=search_params) 

        try:
            results = req.json()['items']
        except:
            messages.error(request,'Enter valid api key Items not found')
            
            return redirect('user_index')
        
        


        ''' video id's extracting to get the video's from the youtube '''

        videos_ids = []
        for results in results:
            videos_ids.append(results['id']['videoId'])
        

        ''' extracting the video's from the youtube using video-id's which we have extracted above'''    

        video_params = {
            'key' : settings.GOOGLE_API,
            'part': 'snippet,contentDetails',
            'id': ','.join(videos_ids)
        }

        video_re = requests.get(video_url, params=video_params)
        res = video_re.json()['items']
        
        videos = []
        for i in res:
            #     url.replace('https://www.youtube.com/watch?v=',"https://youtube.com/embed/")
            video_data = {
                'title':i['snippet']['title'],
                'id': i['id'],
                'url':f'https://youtube.com/embed/{i["id"]}', 
                'duration':int(parse_duration(i['contentDetails']['duration']).total_seconds()/ 60 ),
                'thumbnails':i['snippet']['thumbnails']['high']['url']
            }
            

        ''' Extracting the comments using video-id's based on perticular video '''

        comments = []
        
        for id in videos_ids: 
            ver = 'v3'
            youtube = build( 'youtube',ver, developerKey=settings.GOOGLE_API)

            res = youtube.commentThreads().list(
                part = 'id,snippet,replies',
                # order = 'relevence',
                videoId =id,
                maxResults = 2000,
            )
            responce = res.execute()

            resl = responce['items']
            

            
            comm =[]
            for com in resl:
                

                
                com_ts = {
                    'image':com['snippet']['topLevelComment']['snippet']['authorProfileImageUrl'],
                    'name':com['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                    'comment':com['snippet']['topLevelComment']['snippet']['textDisplay'],
                    'sentiment' : 'neutral'
                }
                
                
            
                sid_obj = SentimentIntensityAnalyzer()
                sentiment_dict = sid_obj.polarity_scores(com_ts['comment'])
                if sentiment_dict['compound'] >= 0.5:
                    sentiments = 'Very Positive'
                elif sentiment_dict['compound'] > 0 and sentiment_dict['compound'] < 0.5:
                    sentiments = 'Positive'
                elif sentiment_dict['compound'] < 0 and sentiment_dict['compound'] >= -0.5:
                    sentiments = 'Negative'
                elif sentiment_dict['compound'] <= -0.5:
                    sentiments = 'Very Negative'
                else:
                    sentiments = 'Neutral'
                com_ts['sentiment'] = sentiments
                comm.append(com_ts) 

               

        
        non_popup = []
        con = 0
        for pop in comm:
            non_popup.append(pop)
            con+=1
            if con > 2:
                break
        
        pos = [sentiment for sentiment in comm if sentiment['sentiment']=='Positive']
        verypos = [sentiment for sentiment in comm if sentiment['sentiment']=='Very Positive']
        nege = [sentiment for sentiment in comm if sentiment['sentiment']=='Negative']
        verynege = [sentiment for sentiment in comm if sentiment['sentiment']=='Very Negative']
       
        neutral = len(comm) - (len(nege) + len(pos) + len(verypos) + len(verynege))
        try:
            positive = float(format(100 * len(pos) / len(comm)))
            verypositive = float(format(100 * len(verypos) / len(comm)))
            negetive = float(format(100 * len(nege) / len(comm)))
            verynegetive = float(format(100 * len(verynege) / len(comm)))
            nutraltotal = float(format(100 * neutral / len(comm)))

        except:
            messages.info(request,'Invalid input Enter again')
            return redirect('user_index')

        vid_senti = None
        if (positive > verypositive and positive > negetive) and (positive >verynegetive and positive > nutraltotal):
            vid_senti = 'positive'
        elif (verypositive > positive and verypositive > negetive) and (verypositive > verynegetive and verypositive > nutraltotal):
            vid_senti = 'very positive'
        elif (negetive > positive and negetive > verypositive) and (negetive > verynegetive and negetive > nutraltotal):
            vid_senti = 'negative'

        elif (verynegetive > positive and verynegetive > verypositive) and (verynegetive > negetive and verynegetive > nutraltotal):
            vid_senti = 'very negative'
        else:
            vid_senti = 'neutral'


        data_1 = VideoModel.objects.create(vid_url = s,vid_url_id = videos_ids[0],vid_sentiment = vid_senti,search_author = auth)
        messages.warning(request, 'Detected Successfully')
        return render(request,"user/user-index.html",{'vid':videos_ids[0],'comm':comm,'non':non_popup,'senti':vid_senti})    

    return render(request,"user/user-index.html")




def user_profile(request):
    user_id=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=user_id)
    # device=DeviceModel.objects.filter(device_user=user_id).count()

    
    if request.method=="POST":
        if len(request.FILES) ==0:
            name=request.POST.get("name")
            
            email=request.POST.get("email")
            password=request.POST.get("password")
            contact=request.POST.get("contact")
            city = request.POST.get("city")
            # photo=request.FILES["photo"]
            user.user_name = name
            
            user.user_email = email
            user.user_password = password
            user.user_contact = contact
            user.user_city =  city
        # user.user_country = country

            user.save()
            if user:
                messages.success(request,"Succesflly Updated")
                return redirect("user_profile")

            else:
                messages.error(request,"No changes detected")
                return redirect("user_profile")
        else:
            if request.method=="POST" and request.FILES['photo']:
                name=request.POST.get("name")
            
                email=request.POST.get("email")
                password=request.POST.get("password")
                contact=request.POST.get("contact")
                city = request.POST.get("city")
                photo=request.FILES["photo"]
                user.user_name = name
                
                user.user_email = email
                user.user_password = password
                user.user_contact = contact
                user.user_city =  city
                user.user_photo = photo
                
                # user.user_country = country

                user.save()
                if user:
                    messages.success(request,"Succesflly Updated")
                    return redirect("user_profile")
                

                    

                else:
                    messages.error(request,"No changes detected")
                    return redirect("user_profile")
    return render(request,"user/user-profile.html",{'user':user})



def user_feedback(request):
    user_id=request.session['user_id']
    user=UserdetailsModel.objects.get(user_id=user_id)
    if request.method == "POST":
        rating=request.POST.get("rating")
        review=request.POST.get("review")
        sid_obj= SentimentIntensityAnalyzer()
        sentinent = sid_obj.polarity_scores(review)
        
        if sentinent["compound"] > 0:
            sent = "positive"
        elif sentinent["compound"] < 0:
            sent = "negative"

        else:
            sent = "neutral"

        if sent:
            feedback = FeedbackModel.objects.create(review=review,rating=rating,reviewer=user,sentiment=sent)
            feedback.save()
            messages.success(request,"Your review has been added succesfully.")
            
            
            return redirect('user_feedback')

        else:
            
            messages.info(request,"Something went wrong, Try again later.")
            return redirect('user_feedback')
    return render(request,"user/user-feedback.html")







