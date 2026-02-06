from django.urls import path
from course.views import FastAPI, courseList

urlpatterns = [
    path('dj/', courseList),
    path('fastapi/', FastAPI)
     
]