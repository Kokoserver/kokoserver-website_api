from django.db import models
from django.db.models import Q
# Create your models here.
from django.db import models
from django.conf import settings


# def blog_upload_image()

class BlogManger(models.Manager):
    def count_blog(self):
        return self.all()
    
    def get_blog(self, id=None):
        return self.get(id=id)
    
    def search_blog(self, params):
        return self.filter(Q(title__icontains=params) | Q(content__icontains=params))
    
    def get_likes(self):
        return self.like.count()
    
    # def get_date(self):
    #     return self



class Blog(models.Model):
    category = models.CharField(max_length=255, default='general')
    title      = models.CharField(max_length=300, verbose_name="blog title")
    body       = models.TextField(verbose_name="blog content", max_length=10000)
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog")
    like       = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="blog_like",  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects    = BlogManger()
    
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("blog", kwargs={"pk": self.pk})
    
    
class BlogComment(models.Model):
    blog   = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="blog")
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog.title
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = 'Comments'
    
    
    
class BlogCategory(models.Model):
        category = models.CharField(max_length=255, default='general', unique=True)
        def __str__(self):
                return self.category
        class Meta:
            verbose_name = "category"
            verbose_name_plural = 'categories'
        
    

    
    
    
    
    
    