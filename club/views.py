from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm

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

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    
    return render(request, 'club/newmeeting.html', {'form':form})

def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    
    return render(request, 'club/newresource.html', {'form':form})