from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'./first_app/index.html')

def about(request):
    return render(request,'./first_app/about.html')
def html_form(request):
    return render(request,'./first_app/html_form.html')
def django_form(request):
    return render(request,'./first_app/django_form.html')