from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import (CreateUserForm, ChangeUserForm)
from .models import User as UserModel
class UserForm(UserAdmin):
    add_form = CreateUserForm
    form = ChangeUserForm
    model = UserModel
    list_display  = ( "id",'email', "tagname", "is_active", "is_staff", "is_staff", 'is_verified')
    list_filter = ( 'is_verified', 'is_active')
    search_fields = ( 'id','email', 'tagname','is_active','is_staff', 'is_verified')
    ordering = ( "id",'tagname', 'is_verified', 'is_active', 'is_staff',)
    list_per_page = 10
    list_display_links = ['email', 'tagname', 'is_active']
    
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
admin.site.unregister(Group)
admin.site.site_header = "KOKOSERVER ADMIN"
admin.site.site_title = "KOKOSERVER Admin Portal"
admin.site.index_title = "Welcome to kokoserver blog Portal"
