from django.urls import path, include
from core import views

urlpatterns = [
    path('',views.home,name="inicio"),
    path('login/',views.login,name="login"),
]