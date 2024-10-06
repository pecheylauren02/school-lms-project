# student_portal/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Grade, Timetable

@login_required  # This decorator ensures that only authenticated users can access the view
def grades_view(request):
    grades = Grade.objects.filter(user=request.user)
    return render(request, 'student_portal/grades.html', {'grades': grades})

@login_required  # Ensure authenticated access for timetable as well
def timetable_view(request):
    timetable = Timetable.objects.filter(user=request.user)
    return render(request, 'student_portal/timetable.html', {'timetable': timetable})
