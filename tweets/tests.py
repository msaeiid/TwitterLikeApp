from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Tweet
from rest_framework.test import APIClient
import json


User = get_user_model()

TEST_USERNAME = 'testuser'
TEST_PASSWORD = 'testpassword'
TWEET_CONTENT = 'my tweet'
TWEET_ACTION_PATH = '/api/tweet/action/'
TWEET_LIST_PATH = '/api/tweet/'
TWEET_CREATE_PATH = '/api/tweet/create/'

CONTENT_TYPE = "application/json"


class UserTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            username=TEST_USERNAME, password=TEST_PASSWORD)
        self.user_b = User.objects.create(
            username='user_b', password='use_b')
        Tweet.objects.create(content=TWEET_CONTENT, user=self.user)
        Tweet.objects.create(content=TWEET_CONTENT, user=self.user)
        Tweet.objects.create(content=TWEET_CONTENT, user=self.user_b)
        self.current_count = Tweet.objects.all().count()

    def test_user_exists(self):
        self.assertEqual(self.user.username, TEST_USERNAME)
        self.assertEqual(self.user.password, TEST_PASSWORD)

    def test_tweet_create(self):
        tweet = Tweet.objects.create(content=TWEET_CONTENT, user=self.user)
        self.assertEqual(tweet.id, 4)
        self.assertEqual(tweet.user, self.user)

    def get_client(self):
        client = APIClient()
        client.force_login(user=self.user)
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get(TWEET_LIST_PATH)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.json()[0]['content'], TWEET_CONTENT)

    def test_tweet_related_name(self):
        user = self.user
        self.assertEqual(user.tweets.count(), 2)

    def test_action_like(self):
        client = self.get_client()
        data = json.dumps({'id': '1', 'action': 'like'})
        response = client.post(path=TWEET_ACTION_PATH,
                               data=data,
                               content_type=CONTENT_TYPE
                               )
        like_count = response.json().get('likes')

        user = self.user
        my_like_instances = user.tweetlike_set.count()
        my_related_likes = user.tweet_user.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(like_count, 1)
        self.assertEqual(my_like_instances, 1)
        self.assertEqual(my_like_instances, my_related_likes)

    def test_action_unlike(self):
        client = self.get_client()
        data = json.dumps({'id': '2', 'action': 'like'})
        response = client.post(
            path=TWEET_ACTION_PATH,
            data=data,
            content_type=CONTENT_TYPE
        )
        self.assertEqual(response.status_code, 200)
        data = json.dumps({'id': '1', 'action': 'unlike'})
        response = client.post(
            path=TWEET_ACTION_PATH,
            data=data,
            content_type=CONTENT_TYPE
        )
        self.assertEqual(response.status_code, 200)

        like_count = response.json().get('likes')
        self.assertEqual(like_count, 0)

    def test_action_retweet(self):
        client = self.get_client()
        data = json.dumps({'id': '2', 'action': 'retweet'})
        response = client.post(path=TWEET_ACTION_PATH,
                               data=data,
                               content_type=CONTENT_TYPE
                               )
        self.assertEqual(response.status_code, 201)
        new_tweet_id = response.json().get('id')
        self.assertNotEqual(2, new_tweet_id)
        self.assertEqual(self.current_count+1, new_tweet_id)

    def test_tweet_create_api_view(self):
        client = self.get_client()
        data = json.dumps({'content': 'This it my test tweet!'})
        response = client.post(path=TWEET_CREATE_PATH,
                               data=data,
                               content_type=CONTENT_TYPE
                               )
        # self.assertEqual(response.status_code, 201)
        # new_tweet_id = response.json().get('id')
        # self.assertEqual(self.current_count+1, new_tweet_id)

    def test_tweet_detail_api_view(self):
        client = self.get_client()
        tweet_detail_id = 1
        path = f'/api/tweet/{tweet_detail_id}/'

        response = client.get(path=path)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('id'), tweet_detail_id)

    def test_tweet_delete_api_view(self):
        client = self.get_client()
        tweet_detail_id = 1
        path = f'/api/tweet/{tweet_detail_id}/delete/'

        response = client.delete(path=path)
        self.assertEqual(response.status_code, 204)
        # again delete  the deleted tweet
        response = client.delete(path=path)
        self.assertEqual(response.status_code, 404)
        # try to delete others users tweet
        response = client.delete(path=f'/api/tweet/3/delete/')
        self.assertEqual(response.status_code, 401)
