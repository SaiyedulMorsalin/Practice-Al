from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'./first_app/index.html')

def about(request):
    
    return render(request,'./first_app/about.html')




def html_form(request):
    if request.method != 'POST':
        return render(request,'./first_app/html_form.html')
    name = request.POST.get('user_name')
    email = request.POST.get('user_email')
    print(name,email)
    return render(request,'./first_app/html_form.html',{'name':name,'email':email})



def django_form(request):
    form = ContactForm(request.POST)
    if form.is_valid():   
        print(form.cleaned_data)
        data = form.cleaned_data
        return render(request,'./first_app/django_form.html',{'form':form,'data':data})
    return render(request,'./first_app/django_form.html',{'form':form})