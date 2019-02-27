from django import forms


class EmployeeAppForm(forms.Form):
    name = forms.CharField()
    dateofbirth = forms.IntegerField()
    positionapplyingfor = forms.CharField()
    salary = forms.IntegerField()