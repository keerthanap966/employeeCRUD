# from turtle import position
from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=200)


class Employee(models.Model):
    Fullname=models.CharField(max_length=200)
    Emp_code=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)

