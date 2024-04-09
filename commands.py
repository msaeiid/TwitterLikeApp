from .tweets.models import TweetLike, Tweet
from django.contrib.auth import get_user_model

User = get_user_model()

# 43-Understanding Setting ManyToManyFields
# In the section he talked about ManyToMany
# by using add(same as a list) we can add likes to


tweet = Tweet.objects.all().first()
print(f'Our tweet\n{tweet}')
user = User.objects.all().first()
print(f'Our user\n{user}')


tweet.likes.add(user)
print(f'add person like\n{tweet.likes.all()}')
tweet.likes.remove(user)
print(f'remove person like\n{tweet.likes.all()}')
tweet.likes.set(User.objects.all())
print(f'add all users to the tweet like\n{tweet.likes.all()}')
empty_users = User.objects.none()
print(f'create empty list of users\n{empty_users}')
tweet.likes.set(empty_users)
print(f'remove all users who like the tweet\n{empty_users}')

# OR

obj = TweetLike.objects.create(user=user, tweet=tweet)
print(f'# we can create directly like below:\n{obj}')


# 51-Verify or Install Nodejs
# installed Nodejs then npm --version and then npx create-react-app


# 9:35:35
# 89-ManyToManyField and Reverse Relations
# in this episode he talks about related_name field on foreign key which we can with them access for the related object versus "(fieldname)_set"
