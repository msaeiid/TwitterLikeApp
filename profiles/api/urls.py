from django.urls import path
from .views import user_follow_view, profile_detail_api_view


app_name = 'tweets_api'

urlpatterns = [
    path('<str:username>/follow/', user_follow_view, name='follow'),
    path('<str:username>/', profile_detail_api_view, name='profile_api'),
]
