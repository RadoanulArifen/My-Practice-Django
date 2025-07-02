from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    # path('home/',views.home,name="home"), #function based
    path('home/',views.StudentLists.as_view(),name="home"),#class based views
    # path('create/',views.create_student, name="create_student"),  #function based
    path('create/',views.CreatrStudent.as_view(), name="create_student"),  #class based view
    # path('edit/<int:id>',views.update_student, name="update_student"), #function based
    path('edit/<int:id>',views.updateStudentData.as_view(), name="update_student"), #class based view
    # path('delete/<int:id>',views.delete_student, name="delete_student"), #function based
    path('delete/<int:id>',views.DeleteStudentData.as_view(), name="delete_student"), #class based view
]
