"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from website.views import welcome, date, about

# We no longer need this import if we are using best practices
# from meetings.views import detail, rooms_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"),   # first argument is the url and the second argument is the view function. The empty string makes it the default
    path('date', date),
    path('about', about),
    path('meetings/', include('meetings.urls'))
# The bottom  lines are replaced by the line above.  This puts the meeting urls inside the meetings "app"
#    path('meetings/<int:id>', detail, name="detailTest"),  # "< >" means it expects an integer after the / and be passed to the view function "detail" as the argument named "id"
#    path('rooms', rooms_list, name="roomTest")
]
