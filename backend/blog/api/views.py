from io import BytesIO
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import  AllowAny,IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from ..models import Blog, BlogComment, BlogCategory
from .serializers import BlogSerializer, BlogCommentSerializer ,CategorySerializer

class BlogApiView(generics.GenericAPIView):
    serializer_class = BlogSerializer
    permission_claases = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    
    def get_queryset(self):
        return super().get_queryset()
    
    def get(self, resquest):
        return
    
class BlogCommentApiView(generics.GenericAPIView):
    def get(self, request):
        return

class BlogCategoryApiView(generics.ListCreateAPIView):
    
    def get(self, request):
        return
