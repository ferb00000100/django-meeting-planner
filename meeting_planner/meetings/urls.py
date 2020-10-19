from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detailTest"), # "< >" means it expects an integer after the / and be passed to the view function "detail" as the argument named "id"
    path('rooms', views.rooms_list, name="roomTest"),
    path('new', views.new, name="new")
]