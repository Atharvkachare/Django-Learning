# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This includes all URLs from your app
    # The 'api/' prefix is optional, but common practice for JSON APIs
    path('api/', include('myapp.urls')), 
]