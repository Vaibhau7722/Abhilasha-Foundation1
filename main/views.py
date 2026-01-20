from django.shortcuts import render, redirect
from .models import Donation, Event, Volunteer
from .forms import DonationForm, VolunteerForm

def home(request):
    events = Event.objects.all()[:3]  # Show latest 3 events
    return render(request, 'home.html', {'events': events})

def donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DonationForm()
    return render(request, 'donation.html', {'form': form})

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def volunteers(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VolunteerForm()
    return render(request, 'volunteers.html', {'form': form})
