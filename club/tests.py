from django.test import TestCase
from django.db import models
from .models import Meeting, MeetingMinutes, Resource, Event
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User 

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
        meet=Meeting(meetingTitle='Python Club Meeting')
        self.meetingID=MeetingMinutes(meetingID=meet)
    
    #This FAILS, and I don't know how to find the right foreign key value to make it PASS.
    def test_ID(self):
        self.assertEqual(str(models.ForeignKey(self.meetingID, on_delete=models.CASCADE)), '1')

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
        self.assertTemplateUsed(response, 'club/index.html')

class GetMeetingTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetings'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'club/meetings.html')

    #def test_view_url_exists_at_desired_location(self):
        #response = self.client.get(reverse('/club/meetings'))
        #self.assertEqual(response.status_code,200)

class GetResourcesTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'club/resources.html')

    #def test_view_url_exists_at_desired_location(self):
        #response = self.client.get(reverse('/club/resources'))
        #self.assertEqual(response.status_code,200)

#This does not work and I don't know why. 
class GetMeetingDetailsTest(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('meetingdetails'))
        self.assertEqual(response.status_code,200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('meetingdetails'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'club/meetingdetails.html')

    #def test_view_url_exists_at_desired_location(self):
        #response = self.client.get(reverse('/club/meetingdetails'))
        #self.assertEqual(response.status_code,200)