from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade, Timetable


@login_required
def grades_view(request):
    grades = Grade.objects.filter(user=request.user)
    return render(request, 'student_portal/grades.html', {'grades': grades})


@login_required
def timetable_view(request):
    timetable = Timetable.objects.filter(user=request.user)
    return render(request, 'student_portal/timetable.html',
                  {'timetable': timetable})
