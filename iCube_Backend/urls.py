"""iCube_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iCube_Application import views as iCube

urlpatterns = [
    path('admin/', admin.site.urls),
    path('verification_code/', iCube.verification_code),
    path('sign_up/', iCube.sign_up),
    path('sign_in/', iCube.sign_in),
    path('article/', iCube.get_article),
    path('image_recognize/', iCube.image_recognize),
    path('face_recognize/', iCube.face_recognize),
    path('image_change_style/', iCube.image_change_style),
    path('upload_image/', iCube.upload_image),
]
