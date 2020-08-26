from rest_framework import serializers 
from ...blog.models import Blog, BlogComment, BlogCategory

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        exclude = "updated_at"
        
    def validate(self, attrs):
        title = super().validate.get('title')
        body  = super().validate.get('body')
        author = super().validate.get('author')
        if len(title) < 4:
            raise serializers.ValidationError("title must be a minimum od 4 characters")
        if len(body) < 10:
            raise serializers.ValidationError("body must be a minimum od 10 characters")
        if author is None:
            raise serializers.ValidationError("please sign in to create blog")
        return super().validate(attrs)
        
        
        
        

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = "__all__"
        
    def validate(self, attrs):
        author = super().validate.get('author', None)
        if author is None:
                raise serializers.ValidationError("please sign in to create blog")
        return super().validate(attrs)
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"
         

