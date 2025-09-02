"""
URL configuration for CareerGuidance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from CareerGuidanceApp.views import *

urlpatterns = [
#//////////////////////////////////////////ADMIN/////////////////////////////////////////

    path('', LoginPage.as_view(), name="LoginPage"),
    path('addcoursePage', addcoursePage.as_view(), name="addcoursePage"),
    path('certificatePage', certificatePage.as_view(), name="certificatePage"),
    path('addCertificatePage', addCertificatePage.as_view(), name="addCertificatePage"),
    path('homepagePage',  homepagePage.as_view(), name="homepagePage"),
    path('UserPage',  UserPage.as_view(), name="UserPage"),
    path('verifycompanyPage',  verifycompanyPage.as_view(), name="verifycompanyPage"),
    path('viewcoursePage',  viewcoursePage.as_view(), name="viewcoursePage"),
    path('viewfeedbackPage',  viewfeedbackPage.as_view(), name="viewfeedbackPage"),
    
#//////////////////////////////////////////HR///////////////////////////////////////////////

    path('addjobPage',  addjobPage.as_view(), name="addjobPage"),
    path('hr_registerPage',  hr_registerPage.as_view(), name="hr_registerPage"),
    path('managejobPagee',  managejobPage.as_view(), name="managejobPage"),
    path('homepage',  homepage.as_view(), name="homepage"),
    path('applieduserPage',  applieduserPage.as_view(), name="applieduserPage"),
    path('userPage',  userPage.as_view(), name="userPage"),


    








    
   
    

]
