from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from sections.models import Section
from users.tests.utils import get_admin_user


class SectionTestCase(APITestCase):
    def setUp(self):
        self.user = get_admin_user()
        response = self.client.post('/users/token/', {"email": "tester@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.test_section = Section.objects.create(
            title='test_section',
            description='test_description'
        )

    def test_section_create(self):
        data = {
            'title': 'test_section_create',
            'description': 'test_section_description_create'
        }
        response = self.client.post('/section/create/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['title'], 'test_section_create')

    def test_section_delete(self):
        response = self.client.delete(f'/section/{self.test_section.id}/delete/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_section_detail(self):
        response = self.client.get(f'/section/{self.test_section.id}/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_section')
        self.assertEqual(response.json()['description'], 'test_description')

    def test_section_list(self):
        response = self.client.get('/section/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'][0]['title'], 'test_section')


    def test_section_update(self):
        data = {
            'title': 'test_section_put',
            'description': 'test_description_put',
        }
        response = self.client.put(f'/section/{self.test_section.id}/update/', data=data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'test_section_put')
        self.assertEqual(response.json()['description'], 'test_description_put')