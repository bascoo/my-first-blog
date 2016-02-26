from django.db import models

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length= 250)
	author = models.CharField(max_length=200)
	body = models.TextField()
	date_published = models.DateTimeField('Date Published')
	created_date = models.DateTimeField('Created Date')

	def __unicode__(self):
		return self.title	

	def publish(self):
		self.date_published = timezone.now()
		self.save()

