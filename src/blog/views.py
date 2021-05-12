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
from rest_framework.pagination import PageNumberPagination

# Create your views here.


@api_view(["GET"])
@permission_classes([])
def blog_list(request):
    """
    List all code blogs, or create a new snippet.
    """
    if request.method == "GET":
        paginator = PageNumberPagination()
        # paginator.page_size = 1
        if 'size' in request.GET:
            paginator.page_size  = request.GET['size']
        blogs = Blog.objects.all()
        result_page = paginator.paginate_queryset(blogs, request)
        # serializer = BlogSerializer(blogs, many=True)
        serializer = BlogSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
@permission_classes([])
def blog_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog_detail = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BlogSerializer(blog_detail)
        return Response(serializer.data)
