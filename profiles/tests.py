from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import json

User = get_user_model()
CONTENT_TYPE = "application/json"

class ProfileTestCase(TestCase):

    def setUp(self) -> None:
        self.first_user = User.objects.create(
            username='first_user', password='213')
        self.second_user = User.objects.create(
            username='second_user', password='123')

    def test_profile_created_via_signal(self):
        qs = User.objects.count()
        self.assertEqual(qs, 2)

    def test_following(self):
        self.first_user.profile.followers.add(self.second_user)
        # add a follower ...
        qs = self.second_user.following.filter(user=self.first_user)
        # from a user, checked user is being followed
        who_first_user_followed = self.first_user.following
        # check first user has no following
        self.assertTrue(qs.exists())
        self.assertFalse(who_first_user_followed.exists())

    def get_client(self):
        client = APIClient()
        client.force_login(user=self.second_user)
        return client

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(
            path=f'/api/profile/{self.first_user}/follow/',
            data=json.dumps({"action": "follow"}),
            content_type=CONTENT_TYPE)
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data.get('count'), 1)

    def test_unfollow_api_endpoint(self):
        # add follower to profile then unfollow it
        self.first_user.profile.followers.add(self.second_user)
        client = self.get_client()
        response = client.post(
            path=f'/api/profile/{self.first_user}/follow/',
            data=json.dumps({"action": "unfollow"}),
            content_type=CONTENT_TYPE)
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data.get('count'), 0)

    # To check user is not following itself
    def test_cannot_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(
            path=f'/api/profile/{self.second_user}/follow/',
            data=json.dumps({"action": "follow"}),
            content_type=CONTENT_TYPE)
        response_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data.get('count'), 0)
