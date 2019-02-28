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
        context = {
            'name': request.POST['name'],
            'dateofbirth':  request.POST ["dateofbirth"],
            'positionapplyingfor': request.POST["positionapplyingfor"],
            'salary': request.POST["salary"],
        }
        return render(request, "gwkenApp/Application.html", context)
    else:
        newForm = EmployeeAppForm()
        context = {
            "newForm": newForm,
        }
        return render(request, "gwkenApp/applicationresults.html", context)