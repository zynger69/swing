from django.db import models

# Create your models here.

from index.models import album

class org_score(models.Model):
  name = models.TextField()
  poster = models.TextField(default="")
  
  def __str__(self):
    return self.name

class channel(models.Model):
  name = models.TextField()
  
  def __str__(self):
    return self.name

class score(models.Model):
  alb = models.ForeignKey(album,default=3,on_delete=models.SET_DEFAULT)
  name = models.ForeignKey(org_score,on_delete=models.CASCADE)
  remixer = models.ForeignKey(channel,on_delete=models.CASCADE)
  link = models.TextField()
  dlink = models.TextField()
  dloads = models.IntegerField(default=0)
  
  def __str__(self):
    return self.name.name+" | "+self.remixer.name 