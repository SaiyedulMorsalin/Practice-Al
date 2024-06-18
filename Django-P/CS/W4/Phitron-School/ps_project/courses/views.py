from django.shortcuts import render

# Create your views here.
def get_course(req):
    return render(req,'base.html')

def profile(req):
    return render(req,'profile.html')