from django.db import models
from datetime import datetime
from mainapp.models import UserdetailsModel
# Create your models here.


class FeedbackModel(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(UserdetailsModel,on_delete=models.CASCADE, related_name='reviewer',null=True)
    
    review = models.CharField(max_length=500, blank=False,null=True)
    rating = models.IntegerField(blank=False,null=True)
    sentiment = models.CharField(max_length=50, blank=False,null=True)
    datetime_reviewed = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_feedbacks'

class VideoModel(models.Model):
    vid_id = models.AutoField(primary_key=True)
    vid_url = models.CharField(max_length=150,blank=False,null=True)
    vid_url_id = models.CharField(max_length=100,blank=False,null=True)
    vid_sentiment = models.CharField(max_length=150,blank=False,null=True)
    datetime_searched = models.DateTimeField(auto_now=True)
    search_author = models.ForeignKey(UserdetailsModel,on_delete=models.CASCADE, related_name='search',blank=False,null=True)
    class Meta:
        db_table = 'video_details'
        


