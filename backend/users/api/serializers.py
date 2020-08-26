from ..models import User # users models
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    I use this class to get user instance without 
    creating another one and to update existing user
    """
    class Meta:
        model = User
        fields = ['id', 'tagname', 'email']
    
    """
    Overriding the update  default method, by Updating user instance in which they can pass anything 
    option but it must contains the user 'id or pk'
    """
    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data["password"])
            user.save()
        except KeyError:
            pass
        return user

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User registeration serializer, this will take in user email, 
    tagname and password and return instance of the new user
    """
    # write_only to restrain user from getting there password back
    password = serializers.CharField(write_only=True, style={"input_type":"password"}, min_length=4)
    class Meta:
        model = User
        fields = ['id','tagname', 'email',  'password']
    """
    Overidding default create method to make it more better, to create new user
    """
    def create(self, validated_data):
        user =    super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
      
class UserLoginSerializer(serializers.Serializer):
    """
    Login user with their email and password.
    email: custome email field 
    password: custome password field
    """
    email = serializers.EmailField()
    # write_only to restrain user from getting there password back
    password = serializers.CharField(
        write_only=True, style={"input_type":"password", 
        "placeholder":"password"}, min_length=4)
    def validate(self, validated_data):
        user = authenticate(**validated_data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("invalid credentials")
        
    
        
       