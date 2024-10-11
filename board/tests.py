from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from board.models import Ad, Feedback
from users.models import User


class BulletinBoardTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru", first_name="test", last_name="testovv", password="12345",
                                        role='admin')
        self.ad = Ad.objects.create(title="test", description="testovv", price=12000.0, author=self.user)

        self.client.force_authenticate(user=self.user)

    def test_detail_ad(self):
        url = reverse('board:detail', args=[self.ad.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.ad.title)
        self.assertEqual(float(data.get("price")), self.ad.price)
        self.assertEqual(data.get("description"), self.ad.description)

    def test_create_ad(self):
        url = reverse('board:create')
        data = {'title': 'телефон', 'price': 12000.0, 'author': self.user.pk, 'description': 'хороший телефон'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ad.objects.all().count(), 2)

    def test_update_ad(self):
        url = reverse('board:update', args=[self.ad.pk])
        data = {"title": "Телевизор"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_ad(self):
        url = reverse('board:delete', args=[self.ad.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.all().count(), 0)

    def test_list_ad(self):
        url = reverse('board:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FeedbackTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru", first_name="testovv", last_name="testovv",
                                        password="12345", role='admin')
        self.ad = Ad.objects.create(title="часы", author=self.user, description="Ролекс", price=12000.0)
        self.feedback = Feedback.objects.create(text='отличные часы, покупали сыну на др', author=self.user,
                                                ad=self.ad)
        self.client.force_authenticate(user=self.user)

    def test_feedback_update(self):
        url = reverse('board:feedback-update', args=[self.feedback.pk])
        data = {"text": "клавиатура"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_feedback(self):
        url = reverse('board:feedback-detail', args=[self.feedback.pk])
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("text"), self.feedback.text)

    def test_create_feedback(self):
        data = {
            "text": "хорший скоростник",
            "author": self.user.pk,
            "ad": self.ad.pk
        }
        url = reverse('board:feedback-create')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.all().count(), 2)

    def test_delete_feedback(self):
        url = reverse('board:feedback-delete', args=[self.feedback.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Feedback.objects.all().count(), 0)

    def test_list_feedback(self):
        url = reverse('board:feedback-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
