from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import pruebaForms
from django.urls import reverse
from .models import Prueba

def testDislex1(request):
    return render(request,'prueba/testDislex1.html')

def testDislex2(request):
    return render(request,'prueba/testDislex2.html')

def testDislex3(request):
    return render(request,'prueba/testDislex3.html')

def formulario(request):
    formPrueba=pruebaForms()
    if request.method == "POST":
        formPrueba=pruebaForms(data=request.POST)
        if formPrueba.is_valid():
            s1 = request.POST.get("nombre")
            s2 = request.POST.get("fecha_nacimiento")
            s3 = request.POST.get("habla_castellano")
            s4 = request.POST.get("genero")
            p = Prueba(nombre=s1,fecha_nacimiento=s2,habla_castellano=s3,genero=s4)
            p.save()
            return redirect(reverse('testDislex2'))

    return render(request,'prueba/formulario.html',{'form':formPrueba})
