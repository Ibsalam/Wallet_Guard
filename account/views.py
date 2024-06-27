from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse


User = get_user_model()

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:dashboard')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'account/login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect('account:login')
    else:
        return render(request, 'account/signup.html')

def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request, 'account/dashboard.html')
    else:
        return redirect('login')

def contact_view(request):
    return render(request, 'contact.html')

def logout_view(request):
    logout(request)
    return redirect('home')

