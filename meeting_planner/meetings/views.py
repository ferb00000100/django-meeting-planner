from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from .models import Meeting, Room

# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def rooms_list(request):
    return render(request, "meetings/room_list.html", {"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, exclude=[])
# modelform_factory generates a new class knows as modelform This helps create and process html forms.
# Create a model form class based on the Meeting class. Pass the Meeting Class and show all the fields of model so exclude nothing.
# MeetingForm in the newly generated modelform class, That is why it is written with Capitol lettters to show that it's a class


def new(request):
    if request.method == "POST":
        # Form has been submitted, process data
        # request.POST is the data the user typed in
        # This creates a new meeting form object, but this includes the data the user typed into the form
        form = MeetingForm(request.POST)
        if form.is_valid():
            # This saves it to the database
            form.save()
            # Redirects to the welcome view
            return redirect("welcome")
    # If method is not POST it will be GET send and empty form
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

