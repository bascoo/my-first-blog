import datetime

from django.db import models
from django.utils import timezone


class Partner(models.Model):
	name = models.CharField(max_length= 250)
	link = models.CharField(max_length= 300)
	date_published = models.DateTimeField('Date Published')

	def __unicode__(self):
		return self.name	

	def publish(self):
		self.date_published = timezone.now()
		self.save()
