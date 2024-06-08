from django.shortcuts import render
from .forms import ContactForm,StudentData,Valid_P

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
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['files']
            # file_path ='./first_app/upload/'+file.name 
            # with open(file_path,'wb+')  as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            data = form.cleaned_data
            return render(request,'./first_app/django_form.html',{'form':form,'data':data})
    else:
        form = ContactForm()
        return render(request,'./first_app/django_form.html',{'form':form})
    
    
def student_data(request):
    if request.method == 'POST':
        form = StudentData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        data = form.cleaned_data
        return render(request,'./first_app/student_form.html',{'form':form,'data':data})
    else:
        form = StudentData()
        return render(request,'./first_app/student_form.html',{'form':form})

def password_valid(request):
    if request.method == 'POST':
        form = Valid_P(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        data = form.cleaned_data
        return render(request,'./first_app/password_valid.html',{'form':form,'data':data})
    else:
        form = Valid_P()
        return render(request,'./first_app/password_valid.html',{'form':form})
            

    