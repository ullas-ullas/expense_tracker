from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
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
        # create_user method handles password encryption . if using normal create method , then use set_password(pwd) to create encrypted password
    return render(request, 'registration.html')