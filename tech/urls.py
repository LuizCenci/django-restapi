from django.urls import path
from tech.views import *

urlpatterns = [
    path('', index, name='index'),
    path('member', members, name='members'),
    
]