from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from homepage.models import Product
# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User,related_name= 'profile',on_delete=models.CASCADE,primary_key=True)
	name = models.CharField(max_length=50,blank=True)
	address = models.TextField()
	def __str__(self):
		return 'Profile of user: {}'.format(self.user.username)

#To populate when a user is registered by admin page
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
# #used signal 
# post_save.connect(create_user_profile, sender=User)

class History(models.Model):
	User = models.ForeignKey(User)
	bought_items = models.TextField(blank=True)

	def __str__(self):
		return '{}'.format(self.User.username)	