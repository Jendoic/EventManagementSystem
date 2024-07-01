from django.shortcuts import render
from auths.models import CustomUser
from .models import Category, Event, RSVP, Notification
from .serializers import CategorySerializer, EventSerializer, RSVPSerializer, NotificationSerializer
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        today = date.today()
        return self.queryset.filter(start_time__gte=today)
    
    def create(self,request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(organizer=request.user)
        self.notifyEventCreation(serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            if event.organizer!= request.user:
                raise PermissionDenied("You are not the organizer of this event.")
            serializer = EventSerializer(event, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            self.notifyEventUpdate(event)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def destroy(self, request, pk=None):
        try:
            event = Event.objects.get(pk=pk)
            if event.organizer!= request.user:
                raise PermissionDenied("You are not the organizer of this event.")
            event.delete()
            self.notifyEventDeletion(event)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def attendees(self, request, pk=None):
        event = self.get_object()
        rsvps = RSVP.objects.filter(event=event, status__in=['Going'])
        serializer = RSVPSerializer(rsvps, many=True)
        return Response(serializer.data)
    
    def notifyEventCreation(self,event):
        Notification.objects.create(
            user=event.organizer,
            message=f"You have created a new event: {event.title}",
        )
        
    def notifyEventUpdate(self,event):
        rsvps = RSVP.objects.filter(event=event)
        for rsvp in rsvps:
            Notification.objects.create(
                user=rsvp.user,
                message=f"Your attendance status for {event.title} has been updated to {rsvp.status}",
    
            )
            
    def notifyEventDeletion(self, event):
        rsvps = RSVP.objects.filter(event=event)
        for rsvp in rsvps:
            Notification.objects.create(
                user=rsvp.user,
                message=f"The event: {event.title} has been deleted",
        
            )
    
class RSVPViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    
    def create(self, request):
        serializer = RSVPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        self.notifyRsvp(serializer.instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def notifyRsvp(self, rsvp):
        Notification.objects.create(
            user=rsvp.user,
            message=f"Your RSVP for event '{rsvp.event.title}' has been confirmed.",
       
        )
        
        
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    @action(detail=False, methods=['post'])
    def markAsRead(self, request):
        notification_ids = request.data.get('ids', [])
        self.queryset.filter(id__in=notification_ids, user=self.request.user).update(is_read=True)
        return Response({"status": "notification marked as read"},status=status.HTTP_200_OK)
    
