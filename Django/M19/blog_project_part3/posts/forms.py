from django import forms
from .models import PostModel,CommentModel

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ['user']
        
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name','email','body']