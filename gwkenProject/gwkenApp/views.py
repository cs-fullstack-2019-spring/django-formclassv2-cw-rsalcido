from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeAppForm

# Create your views here.

def index(request):
    return HttpResponse('Employee Application')


# FUNCTION FOR THE EmployeeApp
def EmployeeApp(request):

    if(request.method == 'POST'):
        print(request.POST)
        context = {"name": request.POST["name"]}
        return render(request, "EmployeeApp/Application.html", context)
    else:
        newForm = EmployeeAppForm()
        context = {
            "newForm": newForm,
        }
        return render(request, "EmployeeApp/applicationresults.html", context)