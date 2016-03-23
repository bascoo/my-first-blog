from django.db import models

# Create your models here.


class Petition(models.Model):
	petition_title = models.CharField(max_length=100)
	petition_text = models.TextField()
	votes = models.IntegerField(default=0)


	def __unicode__(self):
		return self.petition_title



class Vote(models.Model):
	petition = models.ForeignKey(Petition)
	votes = models.IntegerField(default=0)
	vote_title = models.CharField(max_length=10)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.vote_title