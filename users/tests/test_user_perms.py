from rest_framework.test import APITestCase
from rest_framework import status

from users.tests.utils import get_member_user


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = get_member_user()
        response = self.client.post('/users/token/', {"email": "tester_member@test1.com", "password": "qwerty"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_user_delete(self):
        response = self.client.delete('/users/16/delete/')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_list(self):
        response = self.client.get('/users/')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
