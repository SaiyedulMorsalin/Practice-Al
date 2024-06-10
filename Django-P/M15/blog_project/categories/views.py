from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.
def add_category(request):
    if request.method == 'POST': # user post request krese
        category_form = CategoryForm(request.POST) # user er post request data ekhane capture krlam
        if category_form.is_valid(): # post kora data gula valid kina
            category_form.save() # jdi data valid hoy tahole database e save krbo
            print(category_form.cleaned_data)
            return redirect('add_category') #sob thik thakle take add author ei url e pathiye dibo//
    else:# user normali website e gele blank form pabe
        category_form = CategoryForm()
    return render(request,'add_category.html',{'form':category_form})