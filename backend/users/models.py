
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import timezone
class UserMananger(BaseUserManager):
    def create_user(self, email, password, tagname, **extra_fields):
        if not email:
            raise ValueError("Email is not set")
        if not tagname:
            raise ValueError("Account must have tagname")
        email = self.normalize_email(email)
        user = self.model(email=email, tagname=tagname,**extra_fields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, tagname, **extra_fields):
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get("is_active") is not True:
            raise ValueError(" is superuser must be True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("is active must be True ")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("is staff must be True ")
        if extra_fields.get("is_verified") is not True:
            raise ValueError("is verified must be True ")
        return self.create_user(email, password, tagname, **extra_fields)
        
        
        
        

class User(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email  = models.EmailField(unique=True, max_length=255, verbose_name="Email address")
    tagname = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    objects = UserMananger()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['tagname']
    
    
    def __str__(self):
        return self.tagname
    
    def get_status(self):
        return self.is_verified
    
    def get_date(self):
        return super().date_joined
    
    def get_username(self):
        return self.tagname
    
    @property
    def active(self):
        return super().is_active
    
    @property
    def staff(self):
        return super().is_staff
    
    @property
    def verified(self):
        return self.is_verified
    
    @property
    def superuser(self):
        return super().is_superuser
    
    @property
    def admin(self):
        return super().is_superuser
    