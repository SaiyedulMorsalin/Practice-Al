from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request,'./first_app/index.html',{'form':form})
    
    form = StudentForm()
    return render(request,'./first_app/index.html',{'form':form})