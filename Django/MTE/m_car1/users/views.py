from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,RedirectView
from .forms import UserEditForm,UserRegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import logout
from cars.models import CarModel
from orders.models import UserOrder
from django.contrib.auth.decorators import login_required
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
    # class EditProfile(UpdateView):
    #     model = User
    #     form_class = UserEditForm
    #     template_name = 'edit_profile.html'
    #     success_url = reverse_lazy('user_profile')
    
    @login_required
    def edit_profile(request):
        if request.method == 'POST':
            form = UserEditForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('user_profile')
        else:
            form = UserEditForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})
    
    @login_required
    def user_profile(request):
        
        user = request.user
        user_order = UserOrder.objects.filter(user = user)
        price = UserOrder.objects.filter(user = user)
        total_price = 0
        for item_price in price:
            print(item_price.car.car_price)
            total_price+=item_price.car.car_price
        # total_price = sum(car.car_price for car in price)
        # print(total_price)
        return render(request,'./user_profile.html',{'data':user_order,'total_price':total_price})
except Exception as e:
    print(e)