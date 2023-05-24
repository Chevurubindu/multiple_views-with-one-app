"""
URL configuration for project5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1_string/',app1_string,name='app1_string'),
    path('app1_htmlpage/',app1_htmlpage,name='app1_htmlpage.html'),


    path('app2_string/',app1_string,name='app2_string'),
    path('app2_htmlpage/',app1_htmlpage,name='app2_htmlpage.html'),
]