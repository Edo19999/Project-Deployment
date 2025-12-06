from django.test import TestCase
from rest_framework.test import APIClient  # Если APIClient из DRF; иначе from django.test import Client

class MyTest(TestCase):
    def test_ok(self):
        self.assertTrue(True)

    def test_sample_view(self):
        url = "/api/v1/test/"  # Исправил "/apf/" на "/api/" — проверьте правильный URL в вашем проекте
        client = APIClient()  # Добавил (), чтобы создать экземпляр
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
