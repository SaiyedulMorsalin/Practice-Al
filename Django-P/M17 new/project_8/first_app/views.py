from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Created Successfully')
            messages.warning(request,'Account Created with Warning')
            messages.info(request,'Account Created with wrong info')
            form.save()
            print(form.cleaned_data)
    else:
        form = UserForm()
    return render(request,'index.html',{'form':form})