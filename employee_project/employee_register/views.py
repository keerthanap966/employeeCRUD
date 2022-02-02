from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def employee_list(request):
    return HttpResponse("read")
def employee_form(request):
    return HttpResponse("create&update")
def employee_delete(request):
    return HttpResponse("delete")
