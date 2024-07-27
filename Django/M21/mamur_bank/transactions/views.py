from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Transactions
from .constants import DEPOSIT,WITHDRAW,LOAN,LOAN_PAID
from .forms import DepositForm,WithdrawalForm,LoanRequestForm
# Create your views here.

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = ''
    model = Transactions
    title = ''
    success_url = reverse_lazy('')
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account':self.request.user.account
        })
        return kwargs
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title':self.title
        })
        return context
    
    

class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = "Deposit"
    
    def get_initial(self):
        initial = {'transaction_type':DEPOSIT}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance +=amount
        account.save(
            update_fields = ['balance']
        )
        return super().form_valid(form)
    
    

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawalForm
    title = 'Withdraw'
    
    def get_initial(self):
        initial = {'transaction_type':WITHDRAW}
        return initial
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance +=amount
        account.save(
            update_fields = ['balance']
        )
        
        return super().form_valid(form)