from django.contrib import admin
from .models import (Blog, BlogComment, BlogCategory)
from .forms import BlogForm
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'title','category']
    list_filter = ['author','category']
    search_fields = ['id', 'title','author', 'created_at']
    list_display_links = ['author', 'category']
    list_per_page = 10
    form = BlogForm
admin.site.register(Blog, BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','comment','created_at' ]
    list_filter = ['author', 'comment']
    list_display_links = ['author', 'comment']
    search_fields  = ['id', 'comment', 'author', 'created_at']
    list_per_page = 10
admin.site.register(BlogComment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    search_fields = ['id', 'category']
    list_per_page = 10
    list_display_links = [ 'id','category']
admin.site.register(BlogCategory, CategoryAdmin)
