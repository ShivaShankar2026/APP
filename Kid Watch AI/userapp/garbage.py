# def api_search(request):
   
#     ''' getting all the data from the youtube using api'''

#     if request.method == 'POST':
#         youtybe_search_url = ' https://www.googleapis.com/youtube/v3/search'
#         youtube_video_url = 'https://www.googleapis.com/youtube/v3/videos'
#         # comments_thread_url =' https://www.googleapis.com/youtube/v3/commentThreads' 
#         s = request.POST['search']
#         search_params = {
#             'part': 'snippet',
#             'q' : s,
#             'key' : settings.YOUTUBE_API_KEY,
#             'maxResults':1,
#             'type': 'comments'
#         }
    
#         req = requests.get(youtybe_search_url, params=search_params) 
#         # print(req.text)
#         # print('video-id :',req.json()['items'][0]['id']['videoId'])
#         try:
#             results = req.json()['items']

#         except:
#             print('except')
#             messages.error(request,'Enter valid api key Items not found')
#             return redirect('api_search')
#         # print(results)
       
#         # print("Add new api Key")


#         ''' video id's extracting to get the video's from the youtube '''

#         videos_ids = []
#         for results in results:
#             videos_ids.append(results['id']['videoId'])
        
# #============================ videos section ==============================

#         ''' extracting the video's from the youtube using video-id's which we have extracted above'''    

#         video_params = {
#             'key' : settings.YOUTUBE_API_KEY,
#             'part': 'snippet,contentDetails',
#             'id': ','.join(videos_ids)
#         }

#         video_re = requests.get(youtube_video_url, params=video_params)
#         res = video_re.json()['items']
#         # print(res)
#         videos = []
#         for i in res:
#             #     url.replace('https://www.youtube.com/watch?v=',"https://youtube.com/embed/")
#             video_data = {
#                 'title':i['snippet']['title'],
#                 'id': i['id'],
#                 'url':f'https://youtube.com/embed/{i["id"]}', 
#                 'duration':int(parse_duration(i['contentDetails']['duration']).total_seconds()/ 60 ),
#                 'thumbnails':i['snippet']['thumbnails']['high']['url']
#             }
#             videos.append(video_data)

# #=============================== comments section ============================== 

#         ''' Extracting the comments using video-id's based on perticular video '''

#         comments = []
        
#         for id in videos_ids: 
#             ver = 'v3'
#             youtube = build( 'youtube',ver, developerKey=settings.YOUTUBE_API_KEY)

#             res = youtube.commentThreads().list(
#                 part = 'id,snippet,replies',
#                 # order = 'relevence',
#                 videoId =id,
#                 maxResults = 50,
#             )
#             responce = res.execute()

#             resl = responce['items']
            
#             for com in resl:
#                 com_ts = {
#                     'image':com['snippet']['topLevelComment']['snippet']['authorProfileImageUrl'],
#                     'name':com['snippet']['topLevelComment']['snippet']['authorDisplayName'],
#                     'comment':com['snippet']['topLevelComment']['snippet']['textDisplay']
#                 }
                
#                 come = BeautifulSoup(com_ts['comment'])
#                 a = come.get_text()
#                 # print(a,'plain commentsss')
#                 # comments.append(com_ts)

#                 ''' Translating the comments from all languages in to English '''
#                 if a:
#                     try:
#                         translator = Translator()
#                         trans = translator.detect(a)
                    
#                         if trans.lang != "en":
#                             out = translator.translate(a,dest="en")
#                             comment = out.text
#                             com_ts['comment'] = comment
                           
#                         else:
#                             com_ts['comment'] = a
#                             # comments.append(com_ts)

                    
#                     except:
#                         comment = a 
#                         b = ''.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)"," ",comment).split())
#                         print(b)
#                         com_ts['comment'] = b
                        
#  # =============================  sentiment analysis on youtube video comments  ==================================

#                     # analysis = TextBlob(str(com_ts['comment']))
#                     sen = SentimentIntensityAnalyzer() 
#                     analysis = sen.polarity_scores(com_ts['comment'])
                        
#                     sentiments = ''
                    
#                     # print(analysis['compound'])
#                     if analysis['compound'] >= 0.5:
#                         sentiments = 'Very Positive'
#                     elif analysis['compound'] > 0 and analysis['compound'] < 0.5:
#                         sentiments = 'Positive'
#                     elif analysis['compound'] < 0 and analysis['compound'] >= -0.5:
#                         sentiments = 'Negative'
#                     elif analysis['compound'] <= -0.5:
#                         sentiments = 'Very Negative'
#                     else:
#                         sentiments = 'Neutral'
#                     com_ts['sentiment'] = sentiments
#                     comments.append(com_ts) 

 
# #   ================ overall sentiment analysis in  % =========================

#         pos = [sentiment for sentiment in comments if sentiment['sentiment']=='Positive']
#         verypos = [sentiment for sentiment in comments if sentiment['sentiment']=='Very Positive']
#         nege = [sentiment for sentiment in comments if sentiment['sentiment']=='Negative']
#         verynege = [sentiment for sentiment in comments if sentiment['sentiment']=='Very Negative']
       
#         neutral = len(comments) - (len(nege) + len(pos) + len(verypos) + len(verynege))
#         try:
#             positive = float(format(100 * len(pos) / len(comments))) 
#             verypositive = float(format(100 * len(verypos) / len(comments)))
#             negetive = float(format(100 * len(nege) / len(comments)))
#             verynegetive = float(format(100 * len(verynege) / len(comments)))
#             nutraltotal = float(format(100 * neutral / len(comments)))

#         except:
#             print('Comments not found :Refresh your browser')
#             messages.info(request,'Invalid input Enter again')
#             return redirect('api_search')


#         context = {
#             'videos':videos,
#             'comments':comments,
#             'positive':positive,
#             'verypositive':verypositive,
#             'negetive':negetive,
#             'verynegetive':verynegetive,
#             'neutral':nutraltotal,

#             }
#         return render(request, 'user/api-search.html', context)
#     return render(request, 'user/api-search.html')




# '''9/1/23'''
# '''Dynamic comments with dictionary'''
# comm =[]
#             ur_comm = []
#             # global sttx
#             # sttx = None
#             # print(resl,'my result')
#             for com in resl:
                

                
#                 com_ts = {
#                     'image':com['snippet']['topLevelComment']['snippet']['authorProfileImageUrl'],
#                     'name':com['snippet']['topLevelComment']['snippet']['authorDisplayName'],
#                     'comment':com['snippet']['topLevelComment']['snippet']['textDisplay']
#                 }
#                 text ='اب وقت آ گیا ہے کہ دختر نیک کی خواہش پوری کی جائے اور نعلین سے عزت افزائی کی جائے'
                
#                 # print(com_ts['image'])
#                 # print(com_ts['name'])
#                 ty = com_ts['comment']
#                 try:
#                     if detect(ty) == detect(text):
#                         comm.append(com_ts)
#                         print(ty,'success')
#                 except:
#                     print('except')
#                 # print(type(ty))
                
#                 # profiles = BeautifulSoup(com_ts['name'],features="html.parser")
#                 # p = profiles.get_text()

#                 # imgs = BeautifulSoup(com_ts['image'],features="html.parser")
#                 # im = imgs.get_text()
                

#                 # come = BeautifulSoup(com_ts['comment'],features="html.parser")
                
                
#                 # a = come.get_text()
#                 # dic["comment"] = a
#                 # dic["author"]=p
#                 # dic["images"]=im
        
#                 # print(a,'plain commentsss')
#                 # comments.append(com_ts)
#             #     comm.append(dic)
            
                
#             # for v in comm:
#             #     try:
#             #         ffg = v['comment']
                    
                    
#             #         # print(type(ffg))
#             #         if detect(ffg) == detect(text):
#             #             ur_comm.append(v)
#             #             # print(ffg,'comm')
                        
#             #         else:
#             #             # print(ffg)
#             #             comm.remove(v)
#             #             # print('else')
#             #     except:
#             #         ffg = v['comment']
#             #         # print(ffg,'comm')
#             #         comm.remove(v)
#                     # print('except')