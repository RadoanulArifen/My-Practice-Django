from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def profile(request):
    return HttpResponse('I am in profile')

def home(request):
    return HttpResponse('I am in home page')
