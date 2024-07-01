from django.contrib import admin

from .models import Category, Event, RSVP, Notification

admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Notification)
admin.site.register(RSVP)
