from ast import Return

# from ssl import _PasswordType
from django.db.models import Avg,Max,Min,Sum,Count,StdDev,Variance
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from adminapp.models import *
from mainapp.models import *
from userapp.models import *

# Create your views here.

def main_index(request):
    return render(request,"main/main-index.html")





def main_user_reg(request):
    if request.method == "POST" and request.FILES["photo"] :
        name = request.POST['name']
        email = request.POST.get('email')
        contact = request.POST['contact']
        password = request.POST['password']
        city = request.POST['city']
        photo = request.FILES['photo']
        

        try:
            a = UserdetailsModel.objects.get(user_email=email)
            messages.info(request,"Email already exists,try again with another email")
        
        except:

        
            user_create =UserdetailsModel.objects.create(user_name=name,user_email=email,user_password=password,user_contact=contact,user_city=city,user_photo=photo)
            
            
            if user_create:
                messages.success(request,"successfully Registered")
                return redirect('main_user_reg')
            else:
                messages.error(request,"invalid details ,try again")
                return redirect('main_user_reg')
    return render(request,"main/main-user-reg.html")

def main_about(request):
    return render(request,"main/main-about.html")

def main_contact(request):
    return render(request,"main/main-contact.html")