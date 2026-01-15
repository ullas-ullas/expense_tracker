from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.method == "POST":
        firstname  = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(Q(email = email) | Q(username = username))
        if user.exists():
            messages.info(request, "User exists with same username / email")
            return redirect('registration')
        user = User.objects.create_user(username=username, first_name = firstname, last_name = lastname, email = email , password = password)
        login(request, user)
        return redirect('transaction:homepage')
        # create_user method handles password encryption . if using normal create method , then use set_password(pwd) to create encrypted password
    return render(request, 'registration.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = User.objects.filter(username = username)
        if not user_obj.exists():
            messages.error(request, "User doesn't exist!")
            return redirect("login_user")
        user_obj = authenticate(username = username, password = password)
        if not user_obj:
            messages.error(request , "Wrong credentials!")
            return redirect('login_user')
        login(request, user_obj)
        return redirect('transaction:homepage')
    return render(request, 'login_page.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')
        