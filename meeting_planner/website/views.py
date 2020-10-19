from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("The date is " + str(datetime.now()))

def about(request):
    return HttpResponse(
        "My Name is: Jason Martin "
        "Hobbies: Cycling, Snowboarding, Hiking, Fly Fishing" )