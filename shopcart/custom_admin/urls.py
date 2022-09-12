import imghdr
from django.contrib import admin
from django import views
from django.urls import path,include
from custom_admin import views
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import views as auth_views
from django.conf import settings  
from django.conf.urls.static import static

app_name="custom_admin"

urlpatterns = [

    path("adminlogin/",views.adminlogin,name="admin_login"),
    path("",views.start,name="start"),
  
    path("check/",views.check),
    path("logout/", views.admin_logout,name="logout"),
    path("banners/",views.bannerscheck ,name="banners"),
    path("bannersform/",login_required(views.BannersIndex.as_view()),name="bannersform"),
    path("Delete/",views.Delete.as_view(),name="Delete"),
    path("Edit/<int:id>/" ,views.Edit.as_view(),name="Edit"),
    path("config/",views.Configuration.as_view(),name="config"),
    path("configforms/",views.configurationcheck,name="configforms"),
    path("cms/",views.CMS.as_view(),name="cms"),
    path("cmsforms/",views.cmscheck,name="cmsforms"),
    path("email/",views.Email.as_view(),name="email"),
    path("emailsforms/",views.emailcheck,name="emailforms"),
    path("contacts/",views.Contacts.as_view(),name="contacts"),
    path("contactsforms/",views.contactscheck,name="contactsform"),
    path("category/",views.Category.as_view(),name="category"),
    path("categoryforms/",views.categorycheck,name="categoryform"),
    path("products/",views.Product.as_view(),name="products"),
    path("productsforms/",views.productscheck,name="productsform"),
    path("productscateg/",views.ProductCategory.as_view(),name="productscategories"),
    path("productscategforms/",views.productscategorycheck,name="productscategoriesgform"),



    
    # path("bannersclick/",views.banners_click)

]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)