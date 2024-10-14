from django.shortcuts import render, redirect
from .models import StudentProfile, UploadedFile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse


@login_required
def profile_view(request):
    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        profile = StudentProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # Update the profile with submitted data
        profile.user.first_name = request.POST.get('name')
        profile.student_number = request.POST.get('student_number')
        profile.phone_number = request.POST.get('phone_number')
        profile.user.email = request.POST.get('email')
        profile.address = request.POST.get('address')
        profile.bio = request.POST.get('bio')
        profile.date_of_birth = request.POST.get('date_of_birth')

        # Handle file upload
        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES['profile_picture']

        # Save the user and profile
        profile.user.save()
        profile.save()

        # Redirect to the profile display page
        return redirect('display_profile')

    context = {
        'profile': profile,
    }
    return render(request, 'myprofile/myprofile.html', context)


@login_required
def display_profile(request):
    profile = StudentProfile.objects.get(user=request.user)

    context = {
        'profile': profile,
    }
    return render(request, 'myprofile/display_profile.html', context)


# File upload view (for API Injection Attack demonstration)
@login_required
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        UploadedFile.objects.create(user=request.user, file=filename)
        return HttpResponse(f"File uploaded: {filename}")
    return HttpResponse("No file uploaded.")
