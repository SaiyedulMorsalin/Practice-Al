from django.shortcuts import render,redirect
from .forms import AuthorForm
# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            data = form.cleaned_data
            return render(request,'./add_author.html',{'form':form,'data':data})
    form = AuthorForm()
    return render(request,'./add_author.html',{'form':form})
