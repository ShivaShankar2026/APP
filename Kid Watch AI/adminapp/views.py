from ast import Return

# from ssl import _PasswordType
from django.db.models import Avg,Max,Min,Sum,Count,StdDev,Variance
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from adminapp.models import *
from mainapp.models import *
from userapp.models import *
from django.core.paginator import Paginator


# Create your views here.
def main_admin_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print(password)

        if username == "admin" and password == "admin":
            messages.success(request, "Logged In Successfully.")
            return redirect('admin_index')
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect('main_admin_login')
    return render(request,"main/main-admin-login.html")

def admin_index(request):
    pending=UserdetailsModel.objects.filter(user_status="pending").count()
    all=UserdetailsModel.objects.all().count()
    reviews= FeedbackModel.objects.all().count()

    return render(request,"admin/admin-index.html",{'pend':pending,'all':all,'rev':reviews})

def admin_pending_users(request):
    pending=UserdetailsModel.objects.filter(user_status="pending").order_by('-user_id')
    paginator = Paginator(pending,5)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,"admin/admin-pending-users.html",{'pend':page})

def admin_all_users(request):
    all=UserdetailsModel.objects.all().order_by('-user_id')
    paginator = Paginator(all,5)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,"admin/admin-all-users.html",{'all':page})

def admin_searches(request):

    vid = VideoModel.objects.all().order_by('-vid_id')
    paginator = Paginator(vid,5)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,"admin/admin-searches.html",{'vid':page})



def admin_user_feedback(request):
    feedback= FeedbackModel.objects.all().order_by('-feedback_id')
    reviews=FeedbackModel.objects.filter()
    paginator = Paginator(feedback,5)
    page_no = request.GET.get('page')
    page = paginator.get_page(page_no)
    return render(request,"admin/admin-user-feedback.html",{'feed':page})

def admin_sentiment_graph(request):
    pos=FeedbackModel.objects.filter(sentiment="positive").count()
    neu=FeedbackModel.objects.filter(sentiment="neutral").count()
    neg=FeedbackModel.objects.filter(sentiment="negative").count()
    return render(request,"admin/admin-sentiment-graph.html",{'pos':pos,'neu':neu,'neg':neg})


def accept_user(request,user_id):
    accept = get_object_or_404(UserdetailsModel,user_id=user_id)
    accept.user_status = "accepted"
    accept.save(update_fields=["user_status"])
    accept.save()
    if accept:
        messages.success(request,"User Added Successfully")

    return redirect('admin_pending_users')

def decline_user(request,user_id):
    decline = get_object_or_404(UserdetailsModel,user_id=user_id)
    decline.user_status = "declined"
    decline.save(update_fields=["user_status"])
    decline.save()
    if decline:
        messages.success(request,"Rejected Successfully")

    return redirect('admin_pending_users')