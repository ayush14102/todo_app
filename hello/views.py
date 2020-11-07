from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")
    # return HttpResponse("<h1>Hello World!</h1>")

def ayush(request):
    return HttpResponse("<h1>Hello Ayush</h1>")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })
    # return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")