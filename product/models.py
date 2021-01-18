from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=50)
	date = models.DateTimeField()
	image = models.ImageField(upload_to='Images/')
	icon = models.ImageField(upload_to='Images/',default=None)
	votes = models.IntegerField(default=1)
	body = models.CharField(max_length=500)
	url = models.CharField(max_length=200,default=None)
	hunter = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]


	def pub_date(self):
		return self.date.strftime('%b %e %y')
