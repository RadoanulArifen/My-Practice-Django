from django.shortcuts import render , HttpResponse , redirect
from .import models
from . import forms
from django.contrib import messages
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

def create_student(request):
    
    if request.method == 'POST': #user post request korechy
        form = forms.StudentForm(request.POST , request.FILES) #user er post request capture korlam
        if form.is_valid(): #user in put validation korlam
            form.save() #user input save korlam
            messages.add_message(request, messages.SUCCESS, 'Student Created Successfully.')
            return redirect('home')
        
    else:
        form = forms.StudentForm()
    return render(request,'student/create_student.html', {'form':form})

def home(request):
    students = models.Student.objects.all()
    return render(request,'student/index.html', {'students':students})

def update_student(request,id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student) #user er ager data diye fillup korlam
    # form = forms.StudentForm()
    if request.method == 'POST': #user post request korechy
        form = forms.StudentForm(request.POST , request.FILES, instance=student) #user er post request capture korlam
        if form.is_valid(): #user in put validation korlam
            form.save() #user input save korlam
            messages.add_message(request, messages.SUCCESS, 'Student updated Successfully.')
            return redirect('home')
    return render(request,'student/create_student.html', {'form':form, 'edit': True})

def delete_student(request,id):
    student = models.Student.objects.get(id=id) #id wala student k khujy pelam and object o pelam
    student.delete() #oi student k delete korlam
    messages.add_message(request, messages.SUCCESS, 'Student delete Successfully.')
    return redirect('home') #success holy take home page a redirect korlam