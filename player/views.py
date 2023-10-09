from django.shortcuts import render

from django.core.paginator import Paginator
# Create your views here.

from index.models import songs

"""class player_view(DetailView):
  model = songs
  template_name = "player.html"""

def player_view(request,pk,alb__name,name):
  cont = songs.objects.filter(pk=pk)
  list = songs.objects.filter(name="")
  
  song_alb_list = list
  if cont[0].alb.name != "Swing":
    song_alb_list = songs.objects.filter(alb = cont[0].alb)
    song_alb_list = song_alb_list.exclude(pk=cont[0].pk)
  
  words = cont[0].desc.split(" & ")
  for each in words:
    list |= songs.objects.filter(desc__contains=each)
  list = list.distinct()
  list = list.exclude(pk=pk)
  
  for song_in_alb in song_alb_list:
    list = list.exclude(pk=song_in_alb.pk)
  
  list_alb_inc = cont.union(song_alb_list,all=True)
  cont2 = list_alb_inc.union(list,all=True)

  p = Paginator(cont2,1)
  page_number = request.GET.get("page")

  if int(page_number) <= p.num_pages:
    page_obj = p.get_page(page_number)
  else:
    print(int(page_number) % p.num_pages)
    page_obj = p.get_page(int(page_number) % p.num_pages)

  return render(request,"player.html",{"songs" : page_obj[0],"suggs":cont2})