from django.test import TestCase
from django.db import models
from .models import Meeting, MeetingMinutes, Resource, Event
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User 
from .forms import MeetingForm, ResourceForm

# Create your tests here.

# model tests.
class MeetingTest(TestCase):
    def setUp(self):
        self.meetingTitle=Meeting(meetingTitle='Python Club Meeting')

    def test_string(self):
        self.assertEqual(str(self.meetingTitle), 'Python Club Meeting')
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinutesTest(TestCase):
    def setUp(self):
        #self.meet=Meeting(meetingTitle='Python Club Meeting')
        self.minute=MeetingMinutes(meetingID=Meeting(meetingTitle='Python Club Meeting'))
        #self.meetingID=MeetingMinutes(meetingID=self.meet)
    
    #This FAILS, and I don't know how to find the right foreign key value to make it PASS.
    def test_ID(self):
        #meet=Meeting(meetingTitle='Python Club Meeting')
        #minute=MeetingMinutes(meetingID=meet)
        self.assertEqual(str(self.minute), '0')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'minutes')

class ResourcesTest(TestCase):
    def setUp(self):
        self.resourceName=Resource(resourceName='Helpful Resource')

    def test_string(self):
        self.assertEqual(str(self.resourceName), 'Helpful Resource')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.eventTitle=Event(eventTitle='Club Meeting')

    def test_string(self):
        self.assertEqual(str(self.eventTitle), 'Club Meeting')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

# views tests.
class IndexTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('club/index.html')

class GetMeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('club/meetings.html')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('/club/meetings'))
        self.assertEqual(response.status_code,200)

class GetResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('club/resources.html')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(reverse('/club/resources'))
        self.assertEqual(response.status_code,200)

#This does not work and I don't know why. 
class GetMeetingDetailsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingdetails'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingdetails'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('club/meetingdetails.html')

    #def test_view_url_exists_at_desired_location(self):
        #response = self.client.get(reverse('/club/meetingdetails'))
        #self.assertEqual(response.status_code,200)

#test forms
class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
        'meetingTitle':'meeting',
        'meetingDate':'2021-03-03',
        'meetingTime':'19:00',
        'meetingLocation':'A place',
        'meetingAgenda':'do things'
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)

    #Test is failing, per the video 
    def test_meetingForm_Invalid(self):
        data={'meetingTitle':""}
        form=MeetingForm(data)
        self.assertFalse(form.is_valid)

class NewResourceForm(TestCase):
    #valid form data
    def test_resourceform(self):
        data={
        'resourceName':'resource',
        'resourceType':'helpful',
        'resourceURL':'http://www.twitter.com',
        'dateEntered':'2021-03-03',
        'userID':'stephen',
        'resourceDescription':'a resource'
        }
        form=ResourceForm(data)
        self.assertTrue(form.is_valid)

    #Test is failing, per the video 
    def test_resourceForm_Invalid(self):
        data={'resourceName':""}
        form=ResourceForm(data)
        self.assertFalse(form.is_valid)