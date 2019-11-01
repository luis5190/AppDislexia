from django.urls import path, include
from prueba import views

urlpatterns = [
    path('testDislex1/',views.testDislex1,name="testDislex1"),
    path('testDislex2/',views.testDislex2,name="testDislex2"),
    path('testDislex3/',views.testDislex3,name="testDislex3"),
    path('formulario/',views.formulario,name="formulario"),
]