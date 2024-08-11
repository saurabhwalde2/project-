from django.shortcuts import render
from .models import OrmModel
from django.db.models import Avg,Sum,Max,Min,Count

# Create your views here.
def fetch_data_views(r):
    #Emp_list = OrmModel.objects.all()
    #Emp_list = OrmModel.objects.filter(sal__gt=40000)
    #Emp_list = OrmModel.objects.filter(sal__lt=55000)
    #Emp_list = OrmModel.objects.filter(sal__lte=55000)
    #Emp_list = OrmModel.objects.filter(id__in=[1,6,8])
    #Emp_list = OrmModel.objects.filter(city__istartswith='p')
    #Emp_list = OrmModel.objects.filter(name__istartswith='s')
    #Emp_list = OrmModel.objects.filter(name__iendswith='h')
    Emp_list = OrmModel.objects.filter(name__istartswith='m')

    return render(r,'ormapp/display.html',{'Emp_list': Emp_list})


def aggregated_data_view(request):
    avg_salary = OrmModel.objects.aggregate(avg_salary=Avg('sal'))
    total_salary = OrmModel.objects.aggregate(total_salary=Sum('sal'))
    max_salary = OrmModel.objects.aggregate(max_salary=Max('sal'))
    min_salary = OrmModel.objects.aggregate(min_salary=Min('sal'))
    num_employees = OrmModel.objects.aggregate(num_employees=Count('id'))

    return render(request, 'ormapp/single.html', {
        'avg_salary': avg_salary['avg_salary'],
        'total_salary': total_salary['total_salary'],
        'max_salary': max_salary['max_salary'],
        'min_salary': min_salary['min_salary'],
        'num_employees': num_employees['num_employees']
    })




