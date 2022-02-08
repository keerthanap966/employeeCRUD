from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import Employee_form
# Create your views here.
def employee_list(request):
    return render(request,'employee_list.html')
def employee_form(request):
    form=Employee_form()
    context = {'fromkey':form}
    return render(request,'employee_form.html',context)
def employee_delete(request):
    return HttpResponse("delete")
