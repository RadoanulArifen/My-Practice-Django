from django.shortcuts import render , HttpResponse , redirect
from .import models
from . import forms
from django.contrib import messages
from django.views.generic import ListView , UpdateView ,DeleteView ,CreateView
from django.urls import reverse_lazy
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

class CreatrStudent(CreateView):
    
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_student.html'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Created Successfully.')
        return super().form_valid(form)


def home(request):
    students = models.Student.objects.all()
    return render(request,'student/index.html', {'students':students})


#for class base views
class StudentLists(ListView):
    model = models.Student
    template_name = 'student/index.html'
    context_object_name = 'students'






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

#update student data
class updateStudentData(UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = 'student/create_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        messages.add_message(self.request, messages.SUCCESS, 'Student updated Successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)
        context['edit'] = True
        return context


def delete_student(request,id):
    student = models.Student.objects.get(id=id) #id wala student k khujy pelam and object o pelam
    student.delete() #oi student k delete korlam
    messages.add_message(request, messages.SUCCESS, 'Student delete Successfully.')
    return redirect('home') #success holy take home page a redirect korlam

class DeleteStudentData(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'
    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Student delete Successfully.')
        return super().delete(request, *args, **kwargs) 
        