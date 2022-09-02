import imghdr
from django.contrib import admin
from django import views
from django.urls import path,include
from custom_admin import views
from django.contrib.auth import views as auth_views
from django.conf import settings  
from django.conf.urls.static import static
app_name="custom_admin"
urlpatterns = [
    path("adminlogin/",views.adminlogin,name="admin_login"),
    path("",views.start,name="start"),
    path("check/",views.check),
    path("logout/", views.admin_logout,name="logout"),
    path("banners/",views.banners_check ,name="banners"),
    path("bannersform/",views.banners_index.as_view(),name="bannersform"),
    # path("bannersclick/",views.banners_click)
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)