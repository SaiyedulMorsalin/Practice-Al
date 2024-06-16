from django.shortcuts import render
from .forms import CategoryForm
# Create your views here.
def add_category(request):
    form = CategoryForm()
    return render(request,'./category_add.html',{'form':form})