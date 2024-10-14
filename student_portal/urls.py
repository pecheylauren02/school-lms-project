from django.urls import path
from .views import grades_view, timetable_view

urlpatterns = [
    path('grades/', grades_view, name='grades'),
    path('timetable/', timetable_view, name='timetable'),
]
