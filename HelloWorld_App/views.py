from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HelloPage(request):
    return HttpResponse('<h1 style="color:blue"> Hello World..!</h1>')
