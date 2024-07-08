from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class UserCreatingForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    

class UserChangingForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']