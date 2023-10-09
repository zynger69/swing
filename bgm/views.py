from django.shortcuts import render

from .models import *

def bgm_home_view(request):
  return render(request,"bgm/home.html",{})
  
def bgm_player_view(request,pk,name_name,alb_name):
  
  track = score.objects.filter(pk=pk)
  
  sameChannel = score.objects.filter(remixer=track[0].remixer).order_by("-pk")
  
  sameSong = score.objects.filter(name=track[0].name).order_by("-pk")
  
  sameAlb = score.objects.filter(alb=track[0].alb).order_by("-pk")
  
  return render(request,"bgm/player.html",{"bgm":track[0], "sameChannel":sameChannel , "sameAlb":sameAlb,"sameSong":sameSong})
  
def dbgm_view(request,pk):
  track = score.objects.get(pk=pk)
  
  track.dloads = track.dloads + 1
  track.save()
  
  return render(request,"bgm/home.html",{})