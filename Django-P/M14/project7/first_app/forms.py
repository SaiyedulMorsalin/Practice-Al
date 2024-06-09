from django import forms
from . models import StudentModel
class StudentForm(forms.ModelForm):
    class  Meta:
        model = StudentModel
        fields = ['roll','name','address']
        labels = {
            'roll':'Enter Your Roll NO.',
            'name':'Name: ',
            'address':'Enter your Address',
        }
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':"Enter Your Name"}),
            'roll':forms.NumberInput(attrs={'placeholder':"Enter Your Roll"})
        }
        error_messages ={
           'name':{ 'required': "Email is required"},
        }