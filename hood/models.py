from django.db import models

# Create your models here.

class Neighbourhood(models.Model):
  name=models.CharField(max_length =30)
  members=models.IntegerField()
  hood_image=models.ImageField(upload_to='hood/')

