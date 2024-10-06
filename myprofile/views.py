from django.shortcuts import render, redirect
from .models import StudentProfile
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        # Create a new profile if it doesn't exist
        profile = StudentProfile.objects.create(user=request.user)

    context = {
        'profile': profile,
    }
    return render(request, 'myprofile/myprofile.html', context)