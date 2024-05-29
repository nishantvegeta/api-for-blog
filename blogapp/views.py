from rest_framework.decorators import api_view                                                                                     
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializers
from rest_framework import status
from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'index.html', {})


    
@api_view(['GET']) 
def get_all_blogs(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializers(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_blog_by_id(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BlogSerializers(blog)
    return Response(serializer.data)

@api_view(['POST'])
def post_blog(request):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_blog(request, id):
    try:
        blog = Blog.objects.get(pk=id)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = BlogSerializers(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)