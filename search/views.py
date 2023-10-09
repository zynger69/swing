from django.shortcuts import render
from django.contrib import messages

# Create your views here.

import json
from django.http import JsonResponse
from index.models import songs

def search(request):
  
  output = songs.objects.filter(name="")
  
  if request.method == "POST":
    
    inpname = json.loads(request.body).get("inpname")

    output1 = songs.objects.filter(desc__contains=inpname)
    output2 = songs.objects.filter(name__contains=inpname)
      
    output |= output1 
    output |= output2
      
    output = output.distinct()
    
    print(output)
    
    return JsonResponse(list(output.values()),safe=False)