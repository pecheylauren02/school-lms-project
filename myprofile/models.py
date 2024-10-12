from django.db import models
from django.contrib.auth.models import User

# Student profile model
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(blank=True)
    
    # New fields
    student_number = models.CharField(max_length=20, blank=True)  # Student number
    phone_number = models.CharField(max_length=15, blank=True)  # Phone number
    address = models.CharField(max_length=255, blank=True)  # Address

    def __str__(self):
        return self.user.username

# Uploaded file model (for API Injection Attack demonstration)
class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploaded_files/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File uploaded by {self.user.username} on {self.upload_time}"