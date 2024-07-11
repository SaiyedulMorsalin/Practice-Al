from django import forms
from .models import AddCarModel
class AddCarForm(forms.ModelForm):
    class Meta:
        model = AddCarModel
        fields = '__all__'