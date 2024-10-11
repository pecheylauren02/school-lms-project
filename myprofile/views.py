from django.shortcuts import render, redirect
from .models import StudentProfile, UploadedFile
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

# Profile view
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
