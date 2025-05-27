from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return HttpResponse('I am in teachers profile')

def home(request):
    return HttpResponse('I am in teachers home')