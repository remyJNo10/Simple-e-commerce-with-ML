from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=50)
	desc = models.TextField()
	price = models.CharField(max_length=10)
	image = models.ImageField(upload_to="product",blank=True)
	product_tags = models.TextField(blank=True)
	#rating
	def __str__(self):
		return self.name
		