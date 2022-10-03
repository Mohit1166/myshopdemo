from M_Shopify import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'M_Shopify'

urlpatterns =[
    path('',views.main,name="index"),
    path("mylogin/",views.registration.as_view() ,name="mylogin"),
    path('userlogin/',views.login_request,name='userlogin'),
    path('homepage/',views.home_page,name='homepage'),
    
    ]


