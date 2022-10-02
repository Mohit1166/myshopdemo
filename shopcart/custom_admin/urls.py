
from django.contrib import admin
from django import views
from django.urls import path
from custom_admin import views

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings  
# from django.conf.urls.static import static

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
    path("category/",views.Categorys.as_view(),name="category_form"),
    path("categoryforms/",views.categorycheck,name="category"),
    path("categorydelete/",views.CategoryDelete.as_view(),name="category_delete"),
    path("categoryedit/<int:id>/",views.CategoryEdit.as_view(),name="categoryedit"),
    path("products/",views.ProductShop.as_view(),name="products_form"),
    path("productsforms/",views.productscheck,name="products"),
    path("productdelete/",views.ProductDelete.as_view(),name="product_delete"),
    path("productedit/<int:id>/",views.ProductEdit.as_view(),name="productedit"),
    path("productscateg/",views.ProductCategory.as_view(),name="products_categoriesform"),
    path("productscategforms/",views.productscategorycheck,name="productscategory"),
    path("productcategorydelete/",views.ProductCategoryDelete.as_view(),name="product_category_delete"),
    path("productcategoryedit/<int:id>/",views.ProductCategoryEdit.as_view(),name="product_category_edit"),
    path("productsimages/",views.Productimage.as_view(),name="productsimages_form"),
    path("productsimagescheck/",views.productsimagecheck,name="productsimages"),
    path("productimagedelete/",views.ProductImageDelete.as_view(),name="product_image_delete"),
    path("productimageedit/<int:id>/",views.ProductImageEdit.as_view(),name="product_image_edit"),
    path("productattribute/",views.Productattribute.as_view(),name="product_attribute_form"),
    path("productattributecheck/",views.attributecheck,name="productattribute"),
    path("productattributedelete/",views.AttributeDelete.as_view(),name="product_attribute_delete"), 
    path("productattributesedit/<int:id>/",views.ProductAttributeEdit.as_view(),name="product_attribute_edit"),
    path("productvalue/",views.ProductValues.as_view(),name="productvalue_form"),
    path("productvaluecheck/",views.productvaluescheck,name="productvalue"),
    path("productvaluedelete/",views.AttributeValueDelete.as_view(),name="attribute_value_delete"), 
    path("productvalueedit/<int:id>/",views.ProductValueEdit.as_view(),name="product_value_edit"),
    path("productasscos/",views.ProductsAssociation.as_view(),name="productasscos_form"),
    path("productdropdown",views.getAttributeValues,name="productdropdown"),
    path("productasscoscheck/",views.productasscoscheck,name="productasscos"),
    path("user/",views.User.as_view(),name="user"),
    path("usercheck/",views.usercheck,name="usercheck"),
    path("userwishlist/",views.UserWishList.as_view(),name="userwishlist"),
    path("userlistcheck/",views.userlistcheck,name="userlistcheck"),
    path("useraddress/",views.UserAddress.as_view(),name="useraddress"),
    path("useraddresscheck/",views.useraddresscheck,name="useraddresscheck"),
    path("coupons/",views.Discount_Coupons.as_view(),name="coupons_form"),
    path("couponscheck/",views.couponscheck,name="coupons"),
    path("couponsused/",views.CouponsUsed.as_view(),name="couponsused"),
    path("couponsusedcheck/",views.couponsusedcheck,name="couponsusedcheck"),
    path("payment/",views.Payment.as_view(),name="payment_form"),
    path("paymentcheck/",views.paymentcheck,name="payment"),
    path("order/",views.OrderDetails.as_view(),name="order"),
    path("ordercheck/",views.ordercheck,name="ordercheck"),
    path("userorder/",views.UserOrder.as_view(),name="userorder"),
    path("userordercheck/",views.userordercheck,name="userordercheck"),
    
   











    
    # path("bannersclick/",views.banners_click)

]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)