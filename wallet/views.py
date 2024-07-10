from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Budget, Expenses, Income, Report
from .forms import BudgetForm, ExpenseForm, IncomeForm
from django_htmx.http import retarget



def budgets_list(request):
    budgets = Budget.objects.filter(user=request.user)
    context = {
        'budgets': budgets,
    }

    return render(request, 'budgets/budget_overview.html', context)


@login_required
def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            context = {'message': "Budget was added successfully!"}
            return render(request, 'budgets/budget-success.html', context)
        else:
            context = {'form': form}
            return render(request, 'budgets/create_budget.html', context)
    context = {'form': BudgetForm()}
    return render(request, 'budgets/create-budget.html', context)

@login_required
def update_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save()
            context = {'message': "Budget was updated successfully!"}
            return render(request, 'budgets/budget-success.html', context)
        else:
            context = {
                'form': form,
                'budget': budget,
            }
            return render(request, 'budgets/update-budget.html', context)
    context = {
        'form': BudgetForm(instance=budget),
        'budget': budget,
    }
    return render(request, 'budgets/update-budget.html', context)

@login_required
def delete_budget(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    budget.delete()
    context = {
        'message': f"Budget of {budget.amount} was deleted successfully!"
    }
    return render(request, 'budgets/budget-success.html', context)





@login_required
def expenses_list(request):
    expenses = Expenses.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            context = {'message': "Expense was added successfully!", 'form': ExpenseForm()}
            return render(request, 'expenses/expenses_view.html', context)
        else:
            context = {'form': ExpenseForm()}
            return render(request, 'expenses/expenses_view.html', context)
    context = {
        'expenses': expenses,
        'form': ExpenseForm(),
    }

    return render(request, 'expenses/expenses_view.html', context)


@login_required
def update_expense(request, pk):
    expense = get_object_or_404(Expenses, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()
            context = {'message': "Expense was updated successfully!"}
            return render(request, 'expenses/expense-success.html', context)
        else:
            context = {
                'form': form,
                'expense': expense,
            }
            return render(request, 'expenses/update-expense.html', context)
    context = {
        'form': ExpenseForm(instance=expense),
        'expense': expense,
    }
    return render(request, 'expenses/update-expense.html', context)

@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expenses, pk=pk, user=request.user)
    expense.delete()
    context = {
        'message': f"Expense of {expense.amount} was deleted successfully!"
    }
    return render(request, 'expenses/expense-success.html', context)



# Income

def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    context = {
        'incomes': incomes,
    }

    return render(request, 'income/income_overview.html', context)


@login_required
def create_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            context = {'message': "Expense was added successfully!"}
            return render(request, 'income/income-success.html', context)
        else:
            context = {'form': form}
            return render(request, 'income/create_income.html', context)
    context = {'form': IncomeForm()}
    return render(request, 'income/create-income.html', context)

@login_required
def update_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            income = form.save()
            context = {'message': "Expense was updated successfully!"}
            return render(request, 'income/income-success.html', context)
        else:
            context = {
                'form': form,
                'income': income,
            }
            return render(request, 'income/update-income.html', context)
    context = {
        'form': IncomeForm(instance=income),
        'income': income,
    }
    return render(request, 'income/update-income.html', context)

@login_required
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    income.delete()
    context = {
        'message': f"Expense of {income.amount} was deleted successfully!"
    }
    return render(request, 'income/income-success.html', context)



