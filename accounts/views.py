from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


def signup(request):

    if request.method == "POST":

        username = request.POST["username"]

        email = request.POST["email"]

        password = request.POST["password"]

        if User.objects.filter(username=username).exists():

            messages.error(request, "Username already exists")

            return redirect("signup")

        User.objects.create_user(

            username=username,

            email=email,

            password=password

        )

        messages.success(request, "Account Created Successfully")

        return redirect("login")

    return render(request, "signup.html")


def login_user(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user:

            login(request, user)

            return redirect("home")

        else:

            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


def logout_user(request):

    logout(request)

    return redirect("login")