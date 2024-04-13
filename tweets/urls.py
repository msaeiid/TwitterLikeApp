from django.urls import path, include

from tweets.views import (home_view, tweet_detail_view,
                          tweet_list_view, feed_view)
urlpatterns = [
    # path('home/', home_view, name='home'),
    path('', feed_view, name='feed'),
    path('global/', tweet_list_view, name='list'),
    path('<int:tweet_id>/', tweet_detail_view, name='detail')
]
