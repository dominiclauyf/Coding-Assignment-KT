from django.contrib.auth import logout
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return render(request, "index.html")
