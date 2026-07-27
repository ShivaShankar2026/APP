"""ytksa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from turtle import home
from django.contrib import admin
from django.urls import path
from adminapp  import views as adminapp_views
from mainapp import views as mainapp_views
from userapp import views as userapp_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # admin urls
    path('admin-index',adminapp_views.admin_index,name='admin_index'),
    path('admin-pending-users',adminapp_views.admin_pending_users,name='admin_pending_users'),
    path('admin-all-users',adminapp_views.admin_all_users,name='admin_all_users'),
    path('admin-searches',adminapp_views.admin_searches,name='admin_searches'),
    
    path('admin-user-feedback',adminapp_views.admin_user_feedback,name='admin_user_feedback'),
    path('admin-sentiment-graph',adminapp_views.admin_sentiment_graph,name='admin_sentiment_graph'),
    path('admin-accept-user/<int:user_id>',adminapp_views.accept_user,name='accept_user'),
    path('admin-decline-user/<int:user_id>',adminapp_views.decline_user,name='decline_user'),

    # main urls 
    path('',mainapp_views.main_index,name='main_index'),
    path('main-admin-login',adminapp_views.main_admin_login,name='main_admin_login'),
    path('main-user-login',userapp_views.main_user_login,name='main_user_login'),
    path('main-user-reg',mainapp_views.main_user_reg,name='main_user_reg'),
    path('main-about',mainapp_views.main_about,name='main_about'),
    path('main-contact',mainapp_views.main_contact,name='main_contact'),

    #user urls
    path('user-index',userapp_views.user_index,name='user_index'),
    path('user-profile',userapp_views.user_profile,name='user_profile'),
    path('user-feedback',userapp_views.user_feedback,name='user_feedback'),

    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
