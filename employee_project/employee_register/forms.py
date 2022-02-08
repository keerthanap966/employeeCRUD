from django .forms import ModelForm
# from django import forms
from .models import Employee
class Employee_form(ModelForm):
    class Meta:
        model=Employee
        # fields='__all__'
        fields=('Fullname','position')