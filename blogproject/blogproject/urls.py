"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from blogapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('dash/',views.dashboard,name='dash'),
    path('add/',views.addpost,name='add'),
    path('update/<int:id>',views.updatepost,name='update'),
    path('delete/<int:id>',views.deletepost,name='delete'),    
    path('login/',views.loginf,name='loginf'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutf,name='logoutf'),
]
