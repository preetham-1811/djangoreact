# djsr/frontend/urls.py
from django.urls import path, re_path
from .views import * 

urlpatterns = [
    path('', index),  # for the empty url
    re_path(r'^.*/$', index)  # for all other urls
]