from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

# Create your views here.

def home(request):
    if request.user.is_anonymous:
        return redirect("/login", )
    else:
        return render(request, "index.html", {"user": request.user.username})

    return render(request, "index.html")

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return render(request, "index.html")
