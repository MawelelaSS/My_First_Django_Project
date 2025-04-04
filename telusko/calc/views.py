from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'John Doe'})

def add(request):
    val1 = int(request.POST.get('num1', 0))
    val2 = int(request.POST.get('num2', 0))
    res = val1 + val2
    return render(request, 'results.html', {'result': res})