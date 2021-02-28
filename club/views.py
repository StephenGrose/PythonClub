from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html',{'resource_list': resource_list})

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html',{'meeting_list': meeting_list})

def meetingdetails(request, id):
    meet=get_object_or_404(Meeting, pk=id)
    date=meet.meetingDate
    time=meet.meetingTime
    location=meet.meetingLocation
    agenda=meet.meetingAgenda
    context={
        'meet' : meet,
        'date' : date,
        'time' : time,
        'location' : location,
        'agenda' : agenda,
    }
    return render(request, 'club/meetingdetails.html',context=context)

