import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):            
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now


	# was_published_recently.admin_order_field = 'pub_date'

	## no idea why this doesn't work? 
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

# Foreignkey shows a relationship, it can also be many-to-one, many-to-many and one-to-one
class Choise(models.Model):
	question = models.ForeignKey(Question)
	choise_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.choise_text