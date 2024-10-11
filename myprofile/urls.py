from django.urls import path
from .models import profile_view

urlpatterns = [
    path('', profile_view, name='myprofile'),
]