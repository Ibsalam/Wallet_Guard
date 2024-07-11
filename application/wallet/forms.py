from django import forms
from .models import Budget, Expenses, Income


class BudgetForm(forms.ModelForm):

     class Meta:
         model = Budget
         fields = ['name', 'amount']


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = [ 'source', 'amount']



class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = [ 'category', 'amount']
