from django.shortcuts import render
from django.contrib import messages

from django.core.paginator import Paginator
# Create your views here.

import os
from django.conf import settings
from django.http import HttpResponse, Http404

from .models import songs,language,playlist

def lang_view(request,lang__name):
  cont = songs.objects.filter(lang__name=lang__name).order_by('-pk')
  messages.info(request,lang__name)
  return render(request,"home.html",{"songs":cont})

def home_view(request):
  cont = playlist.objects.all().order_by('-pk')
  return render(request,"playlists.html",{"lists":cont})

def playlist_view(request,pk):

  list = playlist.objects.filter(pk=pk)

  for each in list:

    p = Paginator(each.Playlist.all(),1)
    page_number = request.GET.get("page")

    if int(page_number) <= p.num_pages:
      page_obj = p.get_page(page_number)
    else:
      print(int(page_number) % p.num_pages)
      page_obj = p.get_page(int(page_number) % p.num_pages)

    dictionary = {
      "songs" : page_obj[0],
      "suggs":each.Playlist.all(),

    }

  return render(request,"player.html", dictionary)

def sitemap_view(request):
  return render(request,"sitemap.txt",{})

def download_view(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
