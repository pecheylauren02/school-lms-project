from django.urls import path
from .views import profile_view, upload_file

urlpatterns = [
    path('', profile_view, name='myprofile'),
    path('upload/', upload_file, name='upload_file'),  # File upload for API Injection Attack
]