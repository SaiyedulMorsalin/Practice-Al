from django import forms
from django.core import validators
class ContactForm(forms.Form):
    name = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}),error_messages={'required':"Full Name"},help_text='at least 10 characters needed',required=True)
    email = forms.EmailField(label='User Email')
    # age = forms.IntegerField(label='User Age')
    # check = forms.BooleanField()
    birthday = forms.DateField(label='Birthday',widget=forms.DateInput(attrs={'type':'date'}))
    # CHOICES = [('M','Medium'),('L','Large'),('S','Small')]
    # size = forms.ChoiceField(choices=CHOICES)
    # MEALS = [('M','Mash'),('P','Papperoni'),('B','Beef')]
    # pizza = forms.MultipleChoiceField(choices=MEALS)
    # files = forms.FileField(label='Upload File',error_messages={'required':"Please upload a file"})
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'bg-warning text-black','placeholder':'Enter you feedback'}))
    

class StudentData(forms.Form):
    name = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}),error_messages={'required':"Full Name"},help_text='at least 10 characters needed')
    email = forms.CharField(label='User Email',widget=forms.EmailInput(attrs={'placeholder':'Enter your Email'}))
    