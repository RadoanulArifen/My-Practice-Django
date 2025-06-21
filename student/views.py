from django.shortcuts import render , HttpResponse
from .import models
from . import forms
#There are three types of forms in Django
'''
    1.HTML form
    2.Form API
    3.Model form
'''
# Create your views here.
#this is for model form
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name  = request.POST.get('name')
#         email  = request.POST.get('email')
#         phone  = request.POST.get('phone')
#         password  = request.POST.get('password')
#         checkbox  = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')
        
#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False
        
#         student = models.Student(name=name , email=email , phone=phone , password=password,checkbox=checkbox , photo=photo) #student class er object create korlam
#         student.save() #satudent table a record create korlam
#         return HttpResponse("Student object created successfully")
    
    
#     return render(request,'student/index.html')
#this is for model form

def home(request):
    
    if request.method == 'POST': #user post request korechy
        form = forms.StudentForm(request.POST , request.FILES) #user er post request capture korlam
        if form.is_valid(): #user in put validation korlam
            form.save() #user input save korlam
            return HttpResponse("Student Object created successfully")
        
    else:
        form = forms.StudentForm()
    return render(request,'student/index.html', {'form':form})

def student_list(request):
    students = models.Student.objects.all()
    return render(request,'student/index.html', {'students':students})