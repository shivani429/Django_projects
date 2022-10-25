from django.contrib import admin
from django.urls import path
from . import views
from demoapp.views import *
urlpatterns = [

    path('salary',views.salary_list, name='salary_list'),
    path('deletesalary/<int:id>/', views.deletesalary, name='deletesalary'),
    path('update_salary/<int:id>/', views.update_salary, name='update_salary'),
    path('addcontent', views.addcontent, name='addcontent'),
]

    
