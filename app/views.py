from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vamsi(request):
    return HttpResponse('Hi How are you?')

def charan(request):
    return HttpResponse('im good')