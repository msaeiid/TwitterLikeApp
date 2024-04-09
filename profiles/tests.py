from django.test import TestCase
from django.contrib.auth import get_user_model


User = get_user_model()


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
