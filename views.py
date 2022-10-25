from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .models import EmployeeSalary    

#task1 using foreign key
def salary_list(request):
    salary_list = EmployeeSalary.objects.all()
    s = {'salary_list':salary_list}
    return render(request,'salary.html',s)

def deletesalary(request,id):
    salary = EmployeeSalary.objects.get(id=id).delete()
    return redirect('salary_list')

def update_salary(request,id):
    salary = EmployeeSalary.objects.get(id=id)
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee_ = request.POSt.get('employee')
        print('basic_')
        print('hra_')
        print('special_allowance_')
        print('pf_deduction_')
        print('income_tax_')
        print('proffesional_tax_')
        print('convenience_')
        print('lta_')
        print('employee')
        salary.basic = basic_
        salary.hra = hra_
        salary.special_allowance = special_allowance_
        salary.pf_deduction = pf_deduction_
        salary.income_tax = income_tax_
        salary.proffesional_tax = proffesional_tax_
        salary.convenience = convenience_
        salary.lta = lta_
        salary.employee = employee_
        salary.save()
        return redirect('salary_list')
    else:
        a = {'salary':salary}
        return render(request,'update1.html',a)

def addcontent(request):
    employee_list = Employee.objects.all()
    if request.method == 'POST':
        basic_ = request.POST.get('basic')
        hra_ = request.POST.get('hra')
        special_allowance_ = request.POST.get('special_allowance')
        pf_deduction_ = request.POST.get('pf_deduction')
        income_tax_ = request.POST.get('income_tax')
        proffesional_tax_ = request.POST.get('proffesional_tax')
        convenience_ = request.POST.get('convenience')
        lta_ = request.POST.get('lta')
        employee = request.POST.get('employee')
        
        EmployeeSalary.objects.create(basic=basic_, hra=hra_, 
        special_allowance=special_allowance_, pf_deduction=pf_deduction_, 
        income_tax=income_tax_, proffesional_tax=proffesional_tax_, convenience=convenience_, 
        lta=lta_,employee_id=employee)
        return redirect('salary_list')
    else:
        return render(request,'update1.html',{'employee_list':employee_list}



