from django.urls import path
from .views import profile_view, upload_file, delete_profile, display_profile

urlpatterns = [
    path('', profile_view, name='myprofile'),
    path('upload/', upload_file, name='upload_file'),
    path('delete/<int:user_id>/', delete_profile, name='delete_profile'),
    path('display/', display_profile, name='display_profile'),
]
