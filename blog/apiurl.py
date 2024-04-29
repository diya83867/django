from django.urls import path, include
from rest_framework import routers
from blog import api

router = routers.DefaultRouter()
router.register(r'blog', api.ListPostViewSet)
router.register(r'category', api.ListCategoryViewSet)
router.register(r'user', api.ListUserViewSet)
router.register(r'tag', api.ListTagViewSet)
# router.register(r'blog/<int:pk>', api.ListPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]