from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''
Create model classes for the python club database. These should include:
--Meeting--
  fields
    meeting title, 
    meeting date, 
    meeting time, 
    location, 
    Agenda
--Meeting Minutes--
  fields
    meeting id (a foreign key), 
    attendance (a many to many field with User), 
    Minutes text
--Resource--
  fields
    resource name, 
    resource type, 
    URL, 
    date entered, 
    user id (foreign key with User), 
    description
--Event--
  fields
    event title, 
    location, 
    date, 
    time, 
    description,
    user id of the member that posted it (foreign key with User)
'''
class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    meetingLocation=models.TextField()
    meetingAgenda=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.meetingTitle
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingID=models.ForeignKey(Meeting, on_delete=models.CASCADE)
    attendance=models.ManyToManyField(User)
    minutesText=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.meetingID
    
    class Meta:
        db_table = 'minutes'

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    resourceURL=models.URLField()
    dateEntered=models.DateField()
    userID=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    resourceDescription=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    eventLocation=models.TextField()
    eventDate=models.DateField()
    eventTime=models.TimeField()
    eventDescription=models.TextField(null=True,blank=True)
    userID=models.ForeignKey(User,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table='event'

'''
I think location should be separated into its own table since
a location could be used many times. I propose these changes, but 
will not implement these just yet (if at all)

class Location(models.Model):
    locationName=models.CharField(max_length=255)
    locationStreet=models.CharField(max_length=255)
    locationUnit=models.CharField(max_length=16, null=True, blank=True)
    locationCity=models.CharField(max_length=50)
    locationStateAbbr=models.CharField(max_length=2)
    #I am not sure how to validate integer lengths...
    locationPostalCode=models.IntegerField(MinLengthValidator(5,message='Too short'),MaxLengthValidator(5,message='Too long'))

    def __str__(self):
        return self.locationName

    class Meta:
        db_table='location'

class Event(models.Model):
    eventLocation=models.ForeignKey(Location, on_delete.DO_NOTHING)

class Meeting(models.Model):
    meetingLocation=models.ForeignKey(Location, on_delete.DO_NOTHING)
'''
