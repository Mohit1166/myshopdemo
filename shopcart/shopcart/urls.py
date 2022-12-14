"""shopcart URL Configuration

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
from django import views
from django.urls import path,include

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

#Because root and urls of media are in settings so importing settings
from django.conf import settings  
from django.conf.urls.static import static

admin.site.site_header="Developers_Account"
admin.site.site_title="CustomisePanel"
urlpatterns = [
    # path("start/",views.start, name="start"),
    path("admin/",admin.site.urls),
    path('adminpanel/', include("custom_admin.urls")),
    path('', include("M_Shopify.urls"))   
     ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)