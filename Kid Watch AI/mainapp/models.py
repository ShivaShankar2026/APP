from django.db import models
from datetime import datetime
from asyncio.windows_events import NULL
from operator import mod

# Create your models here.

class UserdetailsModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(verbose_name='Name', max_length=50, blank=False,null=False)
    user_email = models.CharField(verbose_name='Email', max_length=100, null=True, blank=True)
    user_password=models.CharField(verbose_name='Password',max_length=100,blank=False,null=False)
    user_contact = models.BigIntegerField(verbose_name='contact', blank=False,null=False)
    user_city = models.CharField(verbose_name='city',max_length=100, blank=False,null=False)
    user_photo = models.FileField(verbose_name='Photo', upload_to='media', blank=False)
    datetime_created = models.DateTimeField(default=datetime.now)
    user_status=models.CharField(default='pending',max_length=50,null=True)
    

    class Meta:
        db_table='user_details'