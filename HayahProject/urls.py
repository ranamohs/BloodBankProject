"""HayahProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
import imp
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path,include
from BloodApp.views import backend3, backend4, login , backend1 , home1 , home2, signup ,backend2 , bloodbank , requests , donorr , needyy , backend4 , backend5 , searchh , Notf
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1', home1 , name='home1'),
    path('form_login', login , name='login'),
    path('backend1' , backend1 , name='backend1'),
    path('home2', home2 , name='home2'),
    path('form_signup', signup , name='signup'),
    path('backend2' , backend2 , name='backend2'),
    path('bloodbank', bloodbank , name='bloodbank'),
    path('requests', requests , name='requests'),
    path('form_donor', donorr , name='donor'),
    path('backend3' , backend3 , name='backend3'),
    path('form_search', needyy , name='needy'),
    path('backend4' , backend4 , name='backend4'),
    path('backend5' , backend5 , name='backend5'),
    path('search', searchh , name='search'),
    path('notification', Notf , name='Notf'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
