from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('auths.urls')),
    path('api/v1/ems/', include('ems.urls')),
]
