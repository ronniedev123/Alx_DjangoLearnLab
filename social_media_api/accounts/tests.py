# accounts/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class FollowFeedTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="ronald", password="pass1234")
        self.user2 = User.objects.create_user(username="brian", password="pass1234")
        self.client.login(username="ronald", password="pass1234")

    def test_follow_and_feed(self):
        # Follow user2
        follow_url = reverse("follow-user", args=[self.user2.id])
        response = self.client.post(follow_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Create a post by user2
        self.client.logout()
        self.client.login(username="brian", password="pass1234")
        Post.objects.create(author=self.user2, content="Brian’s post")

        # Ronald views his feed
        self.client.logout()
        self.client.login(username="ronald", password="pass1234")
        feed_url = reverse("feed")
        response = self.client.get(feed_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Brian’s post", str(response.data))

# Create your tests here.
