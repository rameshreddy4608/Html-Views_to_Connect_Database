from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    LOT=Topic.objects.all()
    d={'topic':LOT}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    LOW=webpage.objects.all()
    e={'web':LOW}
    return render(request,'display_webpage.html',context=e)

def display_accessrecords(request):
    LOA=accessrecords.objects.all()
    d={'access':LOA}
    return render(request,'display_accessrecords.html',context=d)