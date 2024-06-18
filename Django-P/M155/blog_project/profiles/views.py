from django.shortcuts import render
from .forms import ProfilesForm
# Create your views here.
def add_profiles(request):
    if request.method == 'POST':
        form = ProfilesForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'./add_profiles.html',{'form':form})
    else:
        form = ProfilesForm()
        return render(request,'./add_profiles.html',{'form':form})
        