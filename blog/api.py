from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import *
from .seriallizer import *
from rest_framework.response import Response

class ListPostViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """       
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names= ["get", "put", "delete", "patch", "post"]

    # def put(self, request, pk):
    #     save_post = get_object_or_404(Post.objects.all(), pk=pk)
    #     data = request.data.get('post')
    #     serializer = PostSerializer(instance=save_post, data=data, partial=True)
    #     print(save_post, data, serializer)
    #     if serializer.is_valid(raise_exception=True):
    #         save_post = serializer.save()
    #         print(save_post)
    #     return Response({"success": "Post '{}' updated successfully".format(save_post)})

class ListCategoryViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """       
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names= ["get", "put", "delete", "patch", "post"]

class ListUserViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """       
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names= ["get", "put", "delete", "patch", "post"]
    
class ListTagViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """       
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names= ["get", "put", "delete", "patch", "post"]
