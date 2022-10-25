from django.db import models
from datetime import datetime

# Create your models here.

class EmployeeSalary(models.Model):
    basic = models.CharField(max_length=50)
    hra = models.IntegerField()
    special_allowance = models.IntegerField()
    pf_deduction = models.IntegerField()
    income_tax = models.IntegerField()
    proffesional_tax = models.IntegerField()
    convenience = models.IntegerField()
    lta = models.IntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='EmployeeSalary',null=True, blank=True)

    def __str__(self):
        return str(self.basic)



