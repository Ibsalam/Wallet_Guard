from django.contrib import admin

from .models import Budget, Expenses, Income, Report 



admin.site.register(Budget)
admin.site.register(Expenses)
admin.site.register(Report)
admin.site.register(Income)
