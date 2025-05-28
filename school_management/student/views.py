from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def profile(request):
#     return HttpResponse('I am in profile')

def home(request):
    return HttpResponse('I am in home page')

def profile(request):
    
    user_data = {
        "name": "Arifen",
        "age" : 24,
    }
    marks = [
    {   'id': 1,
        "subject":"math",
        "marks": 90
    },
    {
        'id': 2,
        "subject":"english",
        "marks": 85,
    },
    {
        'id': 3,
        "subject":"science",
        "marks": 88 ,
    },
    {
        'id': 4,
        "subject":"history",
        "marks": 92,
    },
    {
        'id': 5,
        "subject":"geography",
        "marks": 87,
    },
    ]
    
    return render(request, 'student/index.html', {'marks': marks})