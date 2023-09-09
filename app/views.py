from django.shortcuts import render

from app.forms import *
from django.http import HttpResponse
from app.models import *

# Create your views here.

def insert_student(request):
    SFEO = StudenntForm()
    d = {'SFEO':SFEO}

    if request.method=='POST':
        SFDO = StudenntForm(request.POST)
        if SFDO.is_valid():
            Sname = SFDO.cleaned_data['Sname']
            Sage = SFDO.cleaned_data['Sage']
            Sid = SFDO.cleaned_data['Sid']
            Semail = SFDO.cleaned_data['Semail']
            SO = Student.objects.get_or_create(Sname=Sname,Sage=Sage,Sid=Sid,Semail=Semail)[0]
            SO.save()
            QSSO = Student.objects.all()
            QSSO = Student.objects.filter(Sname='abcsss').update(Sname='bristi')
            QSSO = Student.objects.filter(Sname='hjkokm').update(Sname='abcde')
            QSSO = Student.objects.filter(Sname='jlkokkm').delete()
            QSSO = Student.objects.all()
            d1 = {'QSSO':QSSO}
            return render(request,'display_student.html',d1)
        else:
            return HttpResponse('Invalid Data')
    return render(request,'insert_student.html',d)