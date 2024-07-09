from django.urls import path
from . import views

app_name = 'wallet'

urlpatterns = [
    path("budgets/", views.budgets_list, name='budgets-list'),
    path('budgets/create/', views.create_budget, name='create-budget'),

    path('budgets/<int:pk>/update/', views.update_budget, name='update-budget'),
    path('budgets/<int:pk>/delete/', views.delete_budget, name='delete-budget'),

    path("expenses/", views.expenses_list, name='expenses-list'),
   # path('expenses/create/', views.create_expense, name='create-expense'),

    path('expenses/<int:pk>/update/', views.update_expense, name='update-expense'),
    path('expenses/<int:pk>/delete/', views.delete_expense, name='delete-expense'),


    path("incomes/", views.income_list, name='incomes-list'),
    path('incomes/create/', views.create_income, name='create-income'),

    path('incomes/<int:pk>/update/', views.update_income, name='update-income'),
    path('incomes/<int:pk>/delete/', views.delete_income, name='delete-income'),

]
