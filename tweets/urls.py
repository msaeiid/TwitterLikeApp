from django.urls import path
from tweets.views import home_view, tweet_detail_view, tweet_list_view, tweet_create_view, tweet_delete_view, tweet_action_view


app_name = 'tweets'

urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<int:pk>/', tweet_detail_view, name='detail'),
    path('delete/<int:pk>/', tweet_delete_view, name='delete'),
    path('action/', tweet_action_view, name='action'),
    path('list/', tweet_list_view, name='list'),
    path('create/', tweet_create_view, name='create')
]
