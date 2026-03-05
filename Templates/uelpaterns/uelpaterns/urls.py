
from django.contrib import admin
from django.urls import path
from app2.views import learn_django
from app3.views import myapp3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learn-django/', learn_django), 
    path('py/', learn_django, {'status' : 'OK'}), 
    path('app3/', myapp3)
]
