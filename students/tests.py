from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Course
from .serializer import CourseSerializer

class RegisterViewTestCase(APITestCase):

    def test_register_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword123',
            'email': 'testuser@example.com'
        }
        response = self.client.post('/api/v1/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')


class CourseViewSetTestCase(APITestCase):

     def setUp(self):
                Course.objects.create(
                    name='Course 1',
                    category='Programming',
                    difficulty='Beginner',
                    time_required='2 hours',
                    session_time='1 hour'
                )
                Course.objects.create(
                    name='Course 2',
                    category='Design',
                    difficulty='Advanced',
                    time_required='4 hours',
                    session_time='2 hours'
                )

    def test_get_courses(self):
                response = self.client.get('/api/v1/courses/')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 2)

    def test_filter_courses_by_category(self):
                response = self.client.get('/api/v1/courses/?category=Programming')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data[0]['name'], 'Course 1')

    def test_filter_courses_by_difficulty(self):
                response = self.client.get('/api/v1/courses/?difficulty=Advanced')
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data[0]['name'], 'Course 2')