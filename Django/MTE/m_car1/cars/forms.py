from django import forms
from .models import CarModel,CommentModel
class AddCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name','email','body']
        
        
class AddCarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'