from django.conf import settings
from django.db import models
from django.utils import timezone


#ok tryna figure out what models to use
#need a model to represent the overall group schedule for an event
#need a model to represent one person's contribution to the group schedule for an event
#ok think I'll just chop the day into 48 half hour blocks
#so the block starting at 00:00 has id 0, 00:30 has id 1
#haha whaaat
class User(models.Model):
    name = models.CharField(max_length=100, default= "John Doe")
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)



#Could use the time blocks to construct a when2meet style view
#Properties would include:
#desired length of event
#a list of which timeblocks are options
#people invited
#use a dict to save for each timeblock which people are available
#and another dict to save for each timeblock which people are unavailable
#since there is a third category of "don't know yet"


class Meeting(models.Model):
    title = models.CharField(max_length=100, default="Meeting")
    description = models.CharField(max_length=200, default="")
    users = models.ManyToManyField(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class TimeSlot(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    meeting = models.ForeignKey(Meeting, related_name='timeslots', on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

