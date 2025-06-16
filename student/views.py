from django.shortcuts import render , HttpResponse
from .import models

#There are three types of forms in Django
'''
    1.HTML form
    2.Form API
    3.Model form
'''
# Create your views here.
def home(request):
    print(request.POST)
    if request.method == 'POST':
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        phone  = request.POST.get('phone')
        password  = request.POST.get('password')
        checkbox  = request.POST.get('checkbox')
        
        if checkbox == 'on':
            checkbox = True
        else:
            checkbox = False
        
        student = models.Student(name=name , email=email , phone=phone , password=password,checkbox=checkbox) #student class er object create korlam
        student.save() #satudent table a record create korlam
        return HttpResponse("Student object created successfully")
    
    
    return render(request,'student/index.html')