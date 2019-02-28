from django.urls import path
from . import views

# path and nickname for the NewHire

urlpatterns = [
    path('', views.index, name="index"),
    path('EmployeeApp/', views.EmployeeApp, name="EmployeeApp"),
]