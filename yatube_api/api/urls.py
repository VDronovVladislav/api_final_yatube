from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register('follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
