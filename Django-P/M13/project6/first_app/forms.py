from django import forms
from django.core import validators
from django.contrib import messages
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
#custome len check function for forms
def len_check(value):
    if len(value) <10:
        raise forms.ValidationError("Enter a value at least 10 chars")
class StudentData(forms.Form):
    # name = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'placeholder':"Enter Your Name"}),error_messages={'required':"Full Name"},help_text='at least 10 characters needed')
    # email = forms.CharField(label='User Email',widget=forms.EmailInput(attrs={'placeholder':'Enter your Email'}))
    name =forms.CharField(widget=forms.TextInput,validators=[validators.MaxLengthValidator(10,message="Maximum Length is 10")])
    email =forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message="Must be a valid email")])
    # check = forms.CharField(widget=forms.CheckboxInput,validators=[validators.ch])
    we = forms.CharField(widget=forms.TextInput,validators=[len_check])
    # def clean(self):
    #     # cleaned_data = super().clean()
    #     user_name = self.cleaned_data['name']
    #     user_email = self.cleaned_data['email']
    #     print(user_name,user_email)
    #     if len(user_name) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")    
    #     if '.com' not in user_email:
    #         raise forms.ValidationError("Your email must contain .com")
    
    
class Valid_P(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your User Name'}),label='User Name')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password'}),label="User Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your Confirm Password'}),label="User Confirm Password")
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_con_pass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if val_con_pass != val_pass:
            raise forms.ValidationError("Password Doesn't Match!!")
        else:
            success = True
        
        
    