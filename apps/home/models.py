from django.db import models
from django.contrib.auth.models import User 

class userProfile(models.Model):
	def url(self,filename):
		path = 'images/usuarios/%s/%s'%(self.user.username,filename)
		return path

	user  = models.OneToOneField(User)
	photo = models.ImageField(upload_to=url)

	def __unicode__(self):
		return self.user.username