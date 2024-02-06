from rest_framework import serializers
from .models import ActivityTracking

class ActivityTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTracking
        fields = '__all__'


