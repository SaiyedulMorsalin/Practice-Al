from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView
from .models import Transactions
from .constants import DEPOSIT,WITHDRAW,LOAN,LOAN_PAID
from .forms import DepositForm,WithdrawalForm,LoanRequestForm
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.views import View
# Create your views here.

class TransactionCreateMixin(LoginRequiredMixin,CreateView):
    template_name = 'transaction_form.html'
    model = Transactions
    title = ''
    success_url = reverse_lazy('transaction_report')
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
        account.balance -=amount
        account.save(
            update_fields = ['balance']
        )
        
        return super().form_valid(form)

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = "Request For Loan"
    
    def get_initial(self):
        initial = {'transaction_type':LOAN}
        return initial
    
    def form_valid(self,form):
        amount = form.cleaned_data.get('amount')
        loan_request_count = Transactions.objects.filter(account = self.request.user.account,transaction_type = LOAN,loan_approve = True).count()
        if loan_request_count >=3:
            return HttpResponse("You have cross the loan limits!!")
        return super().form_valid(form)

class TransactionReportView(LoginRequiredMixin,ListView):
    template_name = ""
    model = Transactions
    balance = 0
    
    def get_queryset(self):
        
        queryset = super().get_queryset().filter(
            account = self.request.user.account,
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str,"%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str,"%Y-%m-%d").date()
            # queryset = queryset.filter(timestamp_date_gte= start_date,timestamp_date_lte = end_date)
            self.balance = Transactions.objects.filter(timestamp_date_gte= start_date,timestamp_date_lte = end_date).aaggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
        
        return queryset.distinct()
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account':self.request.user.account
        })
        return context

class PayLoanView(LoginRequiredMixin,View):
    def get(self,request,loan_id):
        loan = get_object_or_404(Transactions,id = loan_id)
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount <user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('')
                
            else:
                return HttpResponse("Loan Amount is greater than available balance!")
            

class LoanListView(LoginRequiredMixin,ListView):
    model = Transactions
    template_name = ''
    context_object_name = 'loans'
    
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transactions.objects.filter(account = user_account,transaction_type = LOAN)
        return queryset 
    


