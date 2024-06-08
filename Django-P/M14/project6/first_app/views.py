from django.shortcuts import render,redirect
from . import models
# Create your views here.
def index_page (request):
    return render(request,'./first_app/index.html')

def home(request):
    student = models.Student.objects.all()
    # print(student)
    return render(request,'./first_app/home.html',{'data':student})

def delete_student(request,roll):
    std = models.Student.objects.get(pk = roll).delete()
    student = models.Student.objects.all()
    print(std) 
    return redirect('home')