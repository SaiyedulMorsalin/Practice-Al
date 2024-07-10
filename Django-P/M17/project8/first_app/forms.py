from django import forms
from .models import LoginModel,SignUpModel
class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields = '__all__'
        

class SignupForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = '__all__'
        
    