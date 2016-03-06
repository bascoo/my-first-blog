import datetime

from django.db import models
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length= 250)
    description = models.CharField(max_length=1000)
    link = models.CharField(max_length=500) 
    date_event = models.DateTimeField('Event Date')
    image = models.ImageField(upload_to='media/%Y/%m/%d/', blank= True)
    image_title = models.CharField(max_length=20, unique=True, blank = True)
    
    
    
    def __unicode__(self):
		return self.title	
        
    def event_happened(self):    
        now = timezone.now()
        return now <= date_event  