"""BreastCancerDiagnosis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from BreastCancerDiagnosis import views as mainView
from users import views as usr
from admins import views as admins


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainView.index, name='index'),
    path('logout/',mainView.logout, name='logout'),
    path('UserLogin/',mainView.UserLogin, name='UserLogin'),
    path('AdminLogin/',mainView.AdminLogin, name='AdminLogin'),
    path('UserRegister/',mainView.UserRegister, name='UserRegister'),

    ### User Side URLS ####
    path('UserRegisterActions/', usr.UserRegisterActions, name='UserRegisterActions'),
    path('UserLoginCheck/',usr.UserLoginCheck, name='UserLoginCheck'),
    path('UserHome/', usr.UserHome, name='UserHome'),
    path('UserDatapreprocess/', usr.UserDatapreprocess, name='UserDatapreprocess'),
    path('UserClassificationReports/', usr.UserClassificationReports, name='UserClassificationReports'),
    path('UserNeuralNetworks/', usr.UserNeuralNetworks, name='UserNeuralNetworks'),




    ### Admin Login Form ####

    path('AdminLoginCheck/', admins.AdminLoginCheck, name='AdminLoginCheck'),
    path('AdminHome/', admins.AdminHome, name='AdminHome'),
    path('DiagnosisUsers/', admins.DiagnosisUsers, name='DiagnosisUsers'),
    path('AdminActivaUsers/', admins.AdminActivaUsers, name='AdminActivaUsers'),
    path('AdminClassificationReports/', admins.AdminClassificationReports, name='AdminClassificationReports'),
    path('AdminNeuralNetworks/', admins.AdminNeuralNetworks, name='AdminNeuralNetworks'),




]
