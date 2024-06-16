from django import forms 
from .models import ProfilesModel
class ProfilesForm(forms.ModelForm):
    class Meta:
        model = ProfilesModel
        fields = '__all__'