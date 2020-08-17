from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import (CreateUserForm, ChangeUserForm)
from .models import User as UserModel
class UserForm(UserAdmin):
    add_form = CreateUserForm
    form = ChangeUserForm
    model = UserModel
    list_display  = ('email', "tagname", "is_active", "is_staff", "is_staff", 'is_verified')
    list_filter = ('email', 'tagname', 'is_verified', 'is_active', 'is_staff',)
    search_fields = ('email', 'tagname')
    ordering = ('email', 'is_verified', 'is_active', 'is_staff',)
    
    fieldsets = (
        (None, {'fields': ('email', 'tagname','password', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_verified',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tagname', 'password1', 'password2', 'is_staff', 'is_active',)}
        ),
    )

admin.site.register(UserModel, UserForm)
