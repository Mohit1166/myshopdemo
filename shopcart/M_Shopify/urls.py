from M_Shopify import views
from django.urls import path

app_name = 'M_Shopify'

urlpatterns =[
    path('',views.main,name="index"),
    path("mylogin/",views.registration),
]


