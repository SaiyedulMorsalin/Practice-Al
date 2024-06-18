from django.shortcuts import render
from .forms import CategoryForm
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'./category_add.html',{'form':form})
    else:
        form = CategoryForm()
        return render(request,'./category_add.html',{'form':form})