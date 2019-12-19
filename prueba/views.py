from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import pruebaForms, formPreguntas
from django.urls import reverse
from .models import Prueba
from time import sleep

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
            return redirect(reverse('inicioPrueba1'))

    return render(request,'prueba/formulario.html',{'form':formPrueba})

#las vistas del primer examen    
def audio1(request):
    return render(request,'prueba/audio1.html')

def audio2(request):
    return render(request,'prueba/audio2.html')

def audio3(request):
    return render(request,'prueba/audio3.html')

def audio4(request):
    return render(request,'prueba/audio4.html')

def audio5(request):
    return render(request,'prueba/audio5.html')

def audio6(request):
    return render(request,'prueba/audio6.html')


def inicioPrueba1(request):
    return render(request,'prueba/inicioPrueba1.html')

def time1(request):
    return render(request,'prueba/testDislex12')

def testDislex11(request):
    return render(request,'prueba/testDislex11.html')
    
    
    

def testDislex12(request):
    return render(request,'prueba/testDislex12.html')


def testDislex13(request):
    return render(request,'prueba/testDislex13.html')



def inicioPrueba2(request):
    return render(request,'prueba/inicioPrueba2.html')

def testDislex21(request):
    return render(request,'prueba/testDislex21.html')

def testDislex22(request):
    return render(request,'prueba/testDislex22.html')

def testDislex23(request):
    return render(request,'prueba/testDislex23.html')


def inicioPrueba3(request):
    return render(request,'prueba/inicioPrueba3.html')

def testDislex31(request):
    return render(request,'prueba/testDislex31.html')