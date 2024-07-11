from django import forms
from .models import AddCarModel,CommentModel
class AddCarForm(forms.ModelForm):
    class Meta:
        model = AddCarModel
        fields = '__all__'
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name','email','body']