from django.db import models

# Create your models here.

class language(models.Model):
  name = models.CharField(max_length=30)
  
  def __str__(self):
    return self.name

class album(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

class songs(models.Model):
  name = models.CharField(max_length=30)
  alb = models.ForeignKey(album,default=3,on_delete=models.SET_DEFAULT)
  desc = models.CharField(max_length=50)
  spic = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  dlink = models.CharField(max_length=255, default="True")
  lyrics = models.TextField(blank=True)
  lang = models.ForeignKey(language,default=1,on_delete=models.SET_DEFAULT)

  def __str__(self):
    return self.name+" : "+self.desc
    
class playlist(models.Model):
  title = models.CharField(max_length=255)
  displaypic = models.CharField(max_length=255)
  Playlist = models.ManyToManyField(songs)
  
  def __str__(self):
    return self.title
 
