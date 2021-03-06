import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length= 250)
	sec_title = models.CharField(max_length= 250, default="Give secondary title")
	author = models.CharField(max_length=200)
	body = models.TextField()
	date_published = models.DateTimeField('Date Published')
	created_date = models.DateTimeField('Created Date')
	image = models.ImageField(upload_to='media/%Y/%m/%d/')
	image_title = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return self.title	

	def publish(self):
		self.date_published = timezone.now()
		self.save()



