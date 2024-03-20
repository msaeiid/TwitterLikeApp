from django.urls import path
from tweets.views import home_view, tweet_detail_view


app_name = 'tweets'

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pk>/', tweet_detail_view, name='detail_view')
]
