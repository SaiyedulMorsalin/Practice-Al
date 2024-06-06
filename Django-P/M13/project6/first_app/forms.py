from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}),error_messages={'required':"Full Name"},help_text='at least 10 characters needed',required=True)
    email = forms.EmailField(label='User Email')
    age = forms.IntegerField(label='User Age')
    check = forms.BooleanField()
    birthday = forms.DateField(label='Birthday',widget=forms.DateInput(attrs={'type':'date'}))
    
    
    