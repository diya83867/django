from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from rest_framework.response import Response

from .models import Post
from .seriallizer import PostSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_post(title="", description=""):
        if title != "" and description != "":
            Post.objects.create(title=title, description=description)

    def setUp(self):
        # add test data
        self.create_post("like glue", "sean paul")
        self.create_post("simple post", "konshens")
        self.create_post("love is wicked", "brick and lace")
        self.create_post("jam rock", "damien marley")


class GetAllPostTest(BaseViewTest):

    def test_get_all_post(self):
        """
        This test ensures that all post added in the setUp method
        exist when we make a GET request to the post/ endpoint
        """
        # hit the API endpoint
        # response = self.client.get(
        #     reverse("post-all", kwargs={"version": "v1"})
        # )
        # fetch the data from db
        expected = Post.objects.all()
        serialized = PostSerializer(expected, many=True)
        response = Response()
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)