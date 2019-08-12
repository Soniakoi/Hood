from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
  name=models.CharField(max_length =30)
  members=models.IntegerField()
  hood_image=models.ImageField(upload_to='hood/')

class Profile(models.Model):
  name=models.CharField(max_length=60)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  email=models.CharField(max_length=100)
  prof_pic=models.ImageField(upload_to='profiles/')


