from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Welcome to the meeting Planner")

def date(request):
    return HttpResponse("The date is " + str(datetime.now()))

def about(request):
    return HttpResponse(
        "My Name is: Jason Martin "
        "Hobbies: Cycling, Snowboarding, Hiking, Fly Fishing" )