from django.db import models
from auths.models import CustomUser
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)

    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.name
        
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    organizer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    class Meta:
        verbose_name_plural = 'Events'
    
    def __str__(self):
        return self.title
    

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.user.name} is {self.status} to attend {self.event.title}'


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Notifications'
    def __str__(self):
        return self.message[:50] + '...' if len(self.message) > 50 else self.message
    
    
