from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
  name=models.CharField(max_length =30)
  members=models.IntegerField()
  hood_image=models.ImageField(upload_to='hood/')


  def __str__(self):
    return self.name
  def save_hood(self):
    self.save()
  def delete_hood(self):
    self.delete()

  @classmethod
  def view_neigbourhood(cls,neighbourhood_id):
    hood=cls.objects.filter(id=neighbourhood_id)
    return hood

class Profile(models.Model):
  name=models.CharField(max_length=60)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  email=models.CharField(max_length=100)
  prof_pic=models.ImageField(upload_to='profiles/')


  def __str__(self):
    return self.name
  def save_neighbour(self):
    self.save()
  def delete_neighbour(self):
    self.delete()


