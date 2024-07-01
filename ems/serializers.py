from rest_framework import serializers
from django.utils import timezone
from .models import Category, Event, RSVP, Notification


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.StringRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    
    class Meta:
        model = Event
        fields = '__all__'
        
    def validate_start_time(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('Start time cannot be in the past.')
        return value
    
    def validate_end_time(self, value):
        request = self.context.get('request')
        if request and value['value'] <= request.data.get('start_time'):
            raise serializers.ValidationError('End time must be greater than start time.')
        return value

class RSVPSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    event = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all())
    
    class Meta:
        model = RSVP
        fields = '__all__'
    
    def validate_status(self, value):
        if value not in ['Going', 'not Going', 'maybe']:
            raise serializers.ValidationError('Status must be one of attending, not attending, or maybe.')
        return value
    
class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Notification
        fields = '__all__'
    
    def validate_message(self, value):
        if len(value) > 100:
            raise serializers.ValidationError('Message cannot exceed 100 characters.')
        return value