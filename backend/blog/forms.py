from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category','title','body', 'author', 'like']
        
    def clean_title(self):
       data = self.cleaned_data["title"]
       if data is not None:
          return data
       raise forms.ValidationError("Title can not be empty")
   
   
    def clean_content(self):
       data = self.cleaned_data["content"]
       if data is not None:
           return data
       raise forms.ValidationError("A blog content can't be empty")
   
   