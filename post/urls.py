
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('tweet', TweetViewSet, basename='tweet')
router.register('comment', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]