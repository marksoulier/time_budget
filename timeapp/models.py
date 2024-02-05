#create models here for time app
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User

# Activity Tracking Model
class ActivityTracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    hours_spent = models.FloatField()
    day_of_week = models.CharField(max_length=9)

# Goals and Dreams Model
class GoalsDreams(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal = models.TextField()