from django.urls import path, include

from tweets.views import (home_view, tweet_detail_view,
                          tweet_list_view)
urlpatterns = [
    path('', home_view, name='home'),
    path('', tweet_list_view, name='list'),
    path('<int:tweet_id>/', tweet_detail_view, name='detail')
]
