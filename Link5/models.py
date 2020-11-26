from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class part(models.Model):
	name=models.CharField(max_length=300)
	stock=models.IntegerField()
	manufacturing_cost=models.IntegerField()
	selling_cost=models.IntegerField()
	DT=models.DateTimeField(auto_now=True)