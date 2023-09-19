"""
URL configuration for myproject project.

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('les1/', include('myapp.urls')),
    path('', include('myapp.urls')),
    path('les2/', include('myapp2.urls')),
    path('les3/', include('myapp3.urls')),
    path('les4/', include('myapp4.urls')),
    # path('les5/', include('myapp5.urls')),
    # path('sem1/', include('myapp.urls')),
    # path('sem2/', include('seminar2app.urls')),
    # path('sem3/', include('seminar3app.urls')),
    # path('sem4/', include('seminar4app.urls')),
    # path('sem5/', include('seminar5app.urls')),
    # path('__debug__/', include("debug_toolbar.urls")),
    path('les6/', include('myapp6.urls')),
]
