from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Budget, Income, Report, Expenses

# Budget Views
class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budget_list.html'
    
    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    fields = ['name', 'amount']
    template_name = 'budget_form.html'
    success_url = reverse_lazy('budget-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdateView(LoginRequiredMixin, UpdateView):
    model = Budget
    fields = ['name', 'amount']
    template_name = 'budget_form.html'
    success_url = reverse_lazy('budget-list')

class BudgetDeleteView(LoginRequiredMixin, DeleteView):
    model = Budget
    template_name = 'budget_confirm_delete.html'
    success_url = reverse_lazy('budget-list')


# Similar views can be created for Income, Report, and Expenses.
# Following the same pattern as the Budget views, replace 'Budget' with the appropriate model.

# Income Views
class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = 'income_list.html'
    
    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    fields = ['source', 'amount', 'date_added']
    template_name = 'income_form.html'
    success_url = reverse_lazy('income-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ['source', 'amount', 'date_added']
    template_name = 'income_form.html'
    success_url = reverse_lazy('income-list')

class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = 'income_confirm_delete.html'
    success_url = reverse_lazy('income-list')

# Report Views
class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'report_list.html'
    
    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    fields = ['report_type', 'period_start', 'period_end']
    template_name = 'report_form.html'
    success_url = reverse_lazy('report-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    fields = ['report_type', 'period_start', 'period_end']
    template_name = 'report_form.html'
    success_url = reverse_lazy('report-list')

class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'report_confirm_delete.html'
    success_url = reverse_lazy('report-list')

# Expenses Views
class ExpensesListView(LoginRequiredMixin, ListView):
    model = Expenses
    template_name = 'expenses_list.html'
    
    def get_queryset(self):
        return Expenses.objects.filter(user=self.request.user)

class ExpensesCreateView(LoginRequiredMixin, CreateView):
    model = Expenses
    fields = ['category', 'amount', 'date_added']
    template_name = 'expenses_form.html'
    success_url = reverse_lazy('expenses-list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpensesUpdateView(LoginRequiredMixin, UpdateView):
    model = Expenses
    fields = ['category', 'amount', 'date_added']
    template_name = 'expenses_form.html'
    success_url = reverse_lazy('expenses-list')

class ExpensesDeleteView(LoginRequiredMixin, DeleteView):
    model = Expenses
    template_name = 'expenses_confirm_delete.html'
    success_url = reverse_lazy('expenses-list')

