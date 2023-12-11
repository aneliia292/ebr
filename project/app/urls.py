from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    re_path('main/phone/', phone, name='phone'),
]