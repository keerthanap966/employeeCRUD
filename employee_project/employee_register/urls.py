from . import views
from django.urls import path
urlpatterns=[
    path('delete/',views.employee_delete),
    path('list/',views.employee_list),
    path('',views.employee_form),
    
    

    ]