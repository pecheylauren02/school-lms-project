from django.test import TestCase
from django.contrib.auth.models import User
from .models import StudentProfile, UploadedFile

class StudentProfileModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create a StudentProfile instance
        self.student_profile = StudentProfile.objects.create(
            user=self.user,
            date_of_birth='2000-01-01',
            student_number='S123456',
            phone_number='1234567890',
            address='123 Test St, Test City'
        )

    def test_student_profile_creation(self):
        self.assertEqual(self.student_profile.user.username, 'testuser')
        self.assertEqual(self.student_profile.date_of_birth, '2000-01-01')
        self.assertEqual(self.student_profile.student_number, 'S123456')
        self.assertEqual(self.student_profile.phone_number, '1234567890')
        self.assertEqual(self.student_profile.address, '123 Test St, Test City')

    def test_str_method(self):
        self.assertEqual(str(self.student_profile), 'testuser')

class UploadedFileModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create an UploadedFile instance (make sure you have a test file)
        self.uploaded_file = UploadedFile.objects.create(
            user=self.user,
            file='path/to/test/file.txt'  # Change this to a valid test file path in your setup
        )

    def test_uploaded_file_creation(self):
        self.assertEqual(self.uploaded_file.user.username, 'testuser')
        self.assertTrue(hasattr(self.uploaded_file.file, 'url'))  # Check if the file has a URL attribute

    def test_str_method(self):
        self.assertIn('File uploaded by testuser', str(self.uploaded_file))