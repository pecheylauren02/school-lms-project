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
        return redirect('display_profile')  # Change this to the actual URL name for displaying the profile

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
        # Save the uploaded file information in the UploadedFile model
        UploadedFile.objects.create(user=request.user, file=filename)
        return HttpResponse(f"File uploaded: {filename}")
    return HttpResponse("No file uploaded.")

# Admin-only delete view
@login_required
def delete_profile(request, user_id):
    if request.user.is_staff:  # Check if the user is an admin
        user = get_object_or_404(User, id=user_id)
        user.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('home')  # Redirect to home or another page after deletion
    else:
        return HttpResponse("You do not have permission to delete this profile.", status=403)
