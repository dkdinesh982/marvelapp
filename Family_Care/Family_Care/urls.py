"""Family_Care URL Configuration

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
from django.urls import path,include
# from doctor import views
# # from doctor1 import urls

# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('email',views.registerViewSet,basename='email')
# router.register('login',views.LoginViewSet,basename='login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regis/',include('doctor.urls')), 
   
    path('doctor/',include('doctordemo.urls')),
   
    path('patient/',include('patients.urls')),
    path('appointment/',include('Appointment.urls')),
    path('live/',include('live_consulting.urls')),
    path('diagno/',include('diagnostic.urls')),
    path('api/',include('doctorhome.urls')),
   
]
