from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def employee_list(request):
    return render(request,'employee_list.html')
def employee_form(request):
    return render(request,'employee_form.html')
def employee_delete(request):
    return HttpResponse("delete")
