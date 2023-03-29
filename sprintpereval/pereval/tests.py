from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Coords, Level, PerevalAdded, Images, User
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .serializers import UserSerializer

class PerevalSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.coords = Coords.objects.create(name='Test Coords', description='Test Description')
        self.level = Level.objects.create(name='Test Level', description='Test Description')
        self.image = Images.objects.create(title='Test Image', img='test.jpg')
        self.data = {
            'user': {
                'name': 'Test Name',
                'fam': 'Test Fam',
                'otc': 'Test Otc',
                'email': 'test@example.com',
                'phone': '1234567890'
            },
            'coords': {
                'name': 'Test Coords',
                'description': 'Test Description'
            },
            'level': {
                'name': 'Test Level',
                'description': 'Test Description'
            },
            'images': [
                {
                    'title': 'Test Image',
                    'img': 'test.jpg'
                }
            ]
        }

    def test_create_pereval_with_post(self):
        
        url = reverse('pereval-list')
        self.client.force_login(self.user)
        response = self.client.post(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PerevalAdded.objects.count(), 1)
        self.assertEqual(PerevalAdded.objects.get().user.name, 'Test Name')

    def test_update_pereval_with_put(self):
        
        url = reverse('pereval-detail', args=[1])
        self.client.force_login(self.user)
        response = self.client.put(url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PerevalAdded.objects.count(), 1)
        self.assertEqual(PerevalAdded.objects.get().user.name, 'Test Name')

    def test_delete_pereval_with_delete(self):
        
        pereval = PerevalAdded.objects.create(user=self.user, coords=self.coords, level=self.level)
        url = reverse('pereval-detail', args=[pereval.id])
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PerevalAdded.objects.count(), 0)


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='password1',
            first_name='John', last_name='Doe', patronymic='Smith', phone='1234567890')
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='password2',
            first_name='Jane', last_name='Doe', patronymic='Johnson', phone='0987654321')
        self.serializer = UserSerializer(instance=[self.user1, self.user2], many=True)
        self.client = APIClient()

    def test_get_all_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.serializer.data)

    def test_get_single_user(self):
        response = self.client.get('/users/{}/'.format(self.user1.id))
        serializer = UserSerializer(instance=self.user1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create_user(self):
        data = {
            'email': 'newuser@example.com',
            'fam': 'New',
            'name': 'User',
            'otc': 'Test',
            'phone': '1234567890'
        }
        response = self.client.post('/users/', data=data)
        user = User.objects.get(email='newuser@example.com')
        serializer = UserSerializer(instance=user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, serializer.data)

    def test_update_user(self):
        data = {
            'email': 'updateduser@example.com',
            'fam': 'Updated',
            'name': 'User',
            'otc': 'Test',
            'phone': '1234567890'
        }
        response = self.client.put('/users/{}/'.format(self.user1.id), data=data)
        user = User.objects.get(id=self.user1.id)
        serializer = UserSerializer(instance=user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_delete_user(self):
        response = self.client.delete('/users/{}/'.format(self.user1.id))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(id=self.user1.id).exists())