from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,RedirectView
from .forms import UserEditForm,UserRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from cars.models import AddCarModel
# Create your views here.
try:
    class AddUser(CreateView):
        model = User
        form_class = UserRegisterForm
        template_name = 'user_register.html'
        success_url = reverse_lazy('user_login')
        def form_valid(self, form):
            form.save()
            return super().form_valid(form)

    class UserLogin(LoginView):
        template_name = 'user_login.html'
        def get_success_url(self):
            return reverse_lazy('home_page')
        def form_valid(self, form):
            return super().form_valid(form)
        def form_invalid(self, form):
            return  super().form_invalid(form)
        

    class LogoutView(RedirectView)        :
        url = '/user_login'
        def get(self,request,*args,**kwargs):
            logout(request)
            return super(LogoutView,self).get(request,*args,**kwargs)
        
    def user_profile(request):
        data = AddCarModel.objects.all()
        user = request.user.username
        AddCarModel.car_users = user
        
        print(request.user.username)
        
        return render(request,'user_profile.html',{'data':data})
except Exception as e:
    print(e)