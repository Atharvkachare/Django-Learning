# myapp/urls.py
from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
]