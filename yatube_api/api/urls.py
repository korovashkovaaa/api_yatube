from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter
from django.urls import include, path
from api.views import PostViewSet, CommentViewSet, GroupViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='post-comments')
router.register(r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)', CommentViewSet, basename='post-comment')
router.register('groups', GroupViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
