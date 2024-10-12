from django.test import TestCase
from django.contrib.auth.models import User
from .models import Grade, Timetable
import datetime

class GradeModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a Grade instance
        self.grade = Grade.objects.create(
            user=self.user,
            subject='Mathematics',
            score=95.0
        )

    def test_grade_creation(self):
        self.assertEqual(self.grade.user.username, 'testuser')
        self.assertEqual(self.grade.subject, 'Mathematics')
        self.assertEqual(self.grade.score, 95.0)

    def test_str_method(self):
        self.assertEqual(str(self.grade), 'Mathematics: 95.0')


class TimetableModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a Timetable instance using datetime.time
        self.timetable_entry = Timetable.objects.create(
            user=self.user,
            day='Monday',
            subject='Biology',
            time=datetime.time(9, 0)  # Set time as a datetime.time object
        )

    def test_timetable_creation(self):
        self.assertEqual(self.timetable_entry.user.username, 'testuser')
        self.assertEqual(self.timetable_entry.day, 'Monday')
        self.assertEqual(self.timetable_entry.subject, 'Biology')
        self.assertEqual(self.timetable_entry.time.strftime('%H:%M:%S'), '09:00:00')  # This should now work

    def test_str_method(self):
        self.assertEqual(str(self.timetable_entry), 'Monday: Biology at 09:00:00')