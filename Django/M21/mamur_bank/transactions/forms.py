from typing import Any
from django import forms 
from .models import Transactions

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['amount','transaction_type']
    def __init__(self,*args,**kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args,**kwargs)
        self.fields['transaction_type'].disable = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput #user er kach theke hide kra thakbe...
    
    def save(self, commit = True): #chirocena save function
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance # 0 -->5000
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter krbo...
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er filap kra form theke amra amount field er value niye aslam...
        if amount<min_deposit_amount:
            raise forms.ValidationError(f'You need to deposit at least {min_deposit_amount}$')
        return amount


class WithdrawalForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw_balance = 50
        max_withdraw_balance = 25000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount<min_withdraw_balance:
            raise forms.ValidationError(f'You can withdraw at least {min_withdraw_balance}$')
        if amount > max_withdraw_balance:
            raise forms.ValidationError(f'You can withdraw maximum {max_withdraw_balance}$')
        if amount>balance:
            raise forms.ValidationError(f'You have {balance}$ in you account'
                                        'You can not withdraw more than your account balance')
        
        return amount
        

class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount
                    