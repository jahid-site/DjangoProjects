from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return HttpResponse("Welcome to Django!")
    
def bkash(request):
    return HttpResponse('Payments using bkash')
    
    