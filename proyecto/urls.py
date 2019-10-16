"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.login,name="login"),
    path('resultados/',views.resultados,name="resultados"),
    path('testDislex1/',views.testDislex1,name="testDislex1"),
    path('admin/', admin.site.urls),
]
admin.site.site_header ="luis"


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
