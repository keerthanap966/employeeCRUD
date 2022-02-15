from django .forms import ModelForm

#from employee_project.employee_register.views import employee_form
# from django import forms
from .models import Employee
class Employee_form(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        # fields=('Fullname','position')
        labels={'fullname':'FullName','Emp_code':'Employee_Code','mobile':'Mobile','position':'Position'}
        def __init__(self,*args,**kwargs):
            super(Employee_form,self).__init__(*args,**kwargs)
            self.fields['position'].empty_label="select"