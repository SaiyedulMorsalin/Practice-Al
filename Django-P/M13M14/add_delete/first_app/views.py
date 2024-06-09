from django.shortcuts import render
from .forms import StudentForm
from .models import StudentModel
# Create your views here.
def index(request):
    student = StudentModel()
    print(student)
    return render(request,'./first_app/index.html',{'data':student})


def form_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return render(request,'./first_app/form.html',{'form':form})
    form = StudentForm()
    return render(request,'./first_app/form.html',{'form':form})

