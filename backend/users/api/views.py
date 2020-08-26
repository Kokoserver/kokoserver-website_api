import io
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework import mixins
from .serializers import (
    UserRegisterSerializer, 
    UserSerializer,
    UserLoginSerializer)
from  ..models import User # users models
from ..utils import Get_response # users utils

    
    

class UserRegisterApi(GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin, Get_response):
    """
     this class create a user, by accepting there email, password and tagname
     and return and instance of the user.
     The UserRegisterSerializer class accept three parameters email, tagname and password
     The userSerializer is use to return the appropraite user detail 
    """
    serializer_class = UserRegisterSerializer
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(self.Response_Data(UserSerializer, user),
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
             
        
class UserUpdateApi(GenericAPIView, mixins.UpdateModelMixin, Get_response):
    """
    This class update user by accepting eaither any of there details including password,
     but they must provide "id or pk" to identify the user instance
     The UserSerializer class take in any user details and return the updated instance
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_id(self):
          """
          Getting the user id from json data if exist
          """
          stream = io.BytesIO(self.request.body)  
          data = JSONParser().parse(stream)
          id = data.get("id", None)
          return id
    
    def get_object(self):
       """
       Overriding the default get_object method to enhance it ability to search by passed json data
       """
       try:
           id = self.get_id()
           if id is not None:
             user = get_object_or_404(User, id=id)
             return user
       except:
            id = self.kwargs.get("pk", None)
            user = get_object_or_404(User, id=id)
            return user     
           
    def put(self, request, pk=None, *args, **kwargs):
        """
        This method update user instance to update, wich include there
         details, and instance gotten by customize get_object method
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response(self.Response_Data(UserSerializer, user),
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginApi(GenericAPIView, mixins.CreateModelMixin, Get_response):
    """
    This class login users with provided email and password
    """
    serializer_class = UserLoginSerializer
    def post(self, request):
        print(request.body)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            return Response(self.Response_Data(UserSerializer, user),
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserApi(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user
    