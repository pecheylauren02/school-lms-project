from django.urls import path
from .views import profile_view, upload_file, delete_profile, display_profile

urlpatterns = [
    path('', profile_view, name='myprofile'),
    path('upload/', upload_file, name='upload_file'),  # File upload for API Injection Attack
    path('delete/<int:user_id>/', delete_profile, name='delete_profile'),  # Admin delete profile
    path('display/', display_profile, name='display_profile'),  # New URL for profile display
]
