from django.http import HttpResponse

def home(request):
     return HttpResponse ('<h1>Hello!</h1>')

def about(request):
    return HttpResponse ('<h1>This is all about website </h1>')