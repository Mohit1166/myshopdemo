from M_Shopify import views
from django.urls import path
    


app_name = 'M_Shopify'

urlpatterns =[
    path('',views.main,name="index"),
    path("mylogin/",views.registration.as_view() ,name="mylogin"),
    path('userlogin/',views.login_request,name='userlogin'),
    path('homepage/',views.home_page,name='homepage'),
    path('logout/', views.user_logout,name='logout'),
    path('mycart/',views.add_cart,name='cart'),
    path('shopcart/',views.shop_cart,name='showcart')
    ]


