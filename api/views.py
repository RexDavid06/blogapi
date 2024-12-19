from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializers


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "List": "blog-list/",
        "Detail View": "blog-detail/<int:pk>/",
        "Update  View": "blog-update/<int:pk>/",
        "Create View": "blog-create/",
        "Delete View": "blog-delete/<int:pk>/" 
    }
    return Response(api_urls)
    
@api_view(['GET'])
def blog_list(request):
    post = Post.objects.all()
    serializers = PostSerializers(post, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def blogDetail(request, pk):
    post = Post.objects.get(id=pk)
    serializers = PostSerializers(post)
    return Response(serializers.data)

@api_view(['POST'])
def blogUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializers = PostSerializers(post, data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)

@api_view(['POST'])
def blogCreate(request):
    serializers = PostSerializers(data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    
