from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('foodorder')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')


def Signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        rpassword = request.POST.get("rpassword")
        email = request.POST.get("email")
        if password == rpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('Signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('Signup')
            elif User.objects.filter(password=password).exists():
                messages.info(request, "Password already exists")
                return redirect('Signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password is not matching")
            return redirect('Signup')
    return render(request, 'Signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
