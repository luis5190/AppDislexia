from django.urls import path, include
from prueba import views

urlpatterns = [
    path('audio1/',views.audio1,name="audio1"),
    path('audio2/',views.audio2,name="audio2"),
    path('audio3/',views.audio3,name="audio3"),
    path('audio4/',views.audio4,name="audio4"),
    path('audio5/',views.audio5,name="audio5"),
    path('audio6/',views.audio6,name="audio6"),

    path('inicioPrueba1',views.inicioPrueba1,name="inicioPrueba1"),
    path('testDislex11/',views.testDislex11,name="testDislex11"),
    path('testDislex12/',views.testDislex12,name="testDislex12"),
    path('testDislex13/',views.testDislex13,name="testDislex13"),
    path('formulario/',views.formulario,name="formulario"),

    
    path('inicioPrueba2',views.inicioPrueba2,name="inicioPrueba2"),
    path('testDislex21/',views.testDislex21,name="testDislex21"),
    path('testDislex22/',views.testDislex22,name="testDislex22"),
    path('testDislex23/',views.testDislex23,name="testDislex23"),

    path('inicioPrueba3',views.inicioPrueba3,name="inicioPrueba3"),
    path('testDislex31/',views.testDislex31,name="testDislex31"),
]