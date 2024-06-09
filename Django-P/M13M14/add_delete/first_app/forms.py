from django import forms
from .models import StudentModel
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'name':'Enter Your Name',
            'roll':'Enter Your Roll',
        }
