from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def login(request):
    return render(request,'core/login.html')

def resultados(request):
    return render(request,'core/resultados.html')

def testDislex1(request):
    return render(request,'core/testDislex1.html')
