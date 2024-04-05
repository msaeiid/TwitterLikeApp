from django.urls import path
from tweets.api.views import (
    tweet_detail_view,
    tweet_list_view,
    tweet_create_view,
    tweet_delete_view,
    tweet_action_view
)
from django.views.generic import TemplateView


app_name = 'tweets'

urlpatterns = [
    path('', tweet_list_view, name='list'),
    path('action/', tweet_action_view, name='action'),
    path('create/', tweet_create_view, name='create'),
    path('<int:pk>/', tweet_detail_view, name='detail'),
    path('<int:pk>/delete/', tweet_delete_view, name='delete'),
    path('react/', TemplateView.as_view(template_name='react-index.html'),
         name='react-index')
]
