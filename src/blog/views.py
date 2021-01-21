from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from src.blog.models import Blog
from src.blog.serializers import BlogSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.renderers import JSONRenderer
import json

# Create your views here.


@api_view(["GET"])
@permission_classes([])
def blog_list(request):
    """
    List all code blogs, or create a new snippet.
    """
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        with open(
            "/var/www/cosmeticFront/src/data/blog/blog.json", "w" , encoding='utf8'
        ) as outfile:
            json.dump(serializer.data, outfile, indent=4, ensure_ascii=False)
        return Response(serializer.data)


# @api_view(["GET"])
# @permission_classes([])
# def blog_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         blog_detail = Blog.objects.get(pk=pk)
#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = BlogSerializer(blog_detail)
#         return Response(serializer.data)
