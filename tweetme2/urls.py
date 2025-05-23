"""
URL configuration for tweetme2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view, logout_view, registration_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # tweet
    path('', include('tweets.urls')),
    path('api/tweet/', include('tweets.api.urls'), name='tweet'),
    # accounts
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='register'),
    # profile
    path('profile/', include('profiles.urls'), name='profile'),
    path('api/profile/', include('profiles.api.urls'), name='profile')
]

if settings.DEBUG:
    urlpatterns += [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
