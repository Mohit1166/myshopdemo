# from csv import list_dialects
# from email.headerregistry import Address
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from custom_admin.models import Configuration, Cms, Banners,Email,Contacts,Category,Products,ProductsCategory,ProductsImages,ProductAttributes,ProductsAttributesValues,UserWishList,UserAddress,Coupons,CouponsUsed,ProductsAsscos,PaymentGateway,UserOrder,OrderDetails,CustomUser


class configuration_admin(admin.ModelAdmin):
    list_display=("conf_key","conf_value","created_by","date","modify_by","modify_date","modify_status")
admin.site.register(Configuration,configuration_admin) #user model should get connected to info 
# Register your models here.

class Cms_admin(admin.ModelAdmin):
     list_display=("title","content","meta_title","meta_description","meta_keywords","created_by","created_by_date","modify_by","modify_date")
admin.site.register(Cms,Cms_admin)


class banners_admin(admin.ModelAdmin):
    list_display=("Name","banner_path","status_bit")
admin.site.register(Banners,banners_admin)

class Email_admin(admin.ModelAdmin):
    list_display=("title","subject","content","created_by","created_date","modify_by","modify_date")
admin.site.register(Email,Email_admin)

class Contacts_admin(admin.ModelAdmin):
    list_display=("name","email","contact_no","message","note_admin","created_by","created_date",
    "modify_by","modify_date")
admin.site.register(Contacts,Contacts_admin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","parent_id","created_by","created_date","modify_by","modify_date","modify_status")
admin.site.register(Category,CategoryAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display=("name","sku","short_description","long_description","price","special_price",
                  "from_special_price","to_special_price","modify_status","quantity","meta_title","meta_desc",
                  "meta_keywords","modify_status","created_by","created_date","modify_date","modify_by","is_featured")
admin.site.register(Products,ProductsAdmin)

class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display=("product_id","category_id")
admin.site.register(ProductsCategory,ProductsCategoryAdmin)

class ProductsImagesAdmin(admin.ModelAdmin):
    list_display=("image","modify_status","created_by","created_date","modify_by","modify_date",
                  "product_id")
admin.site.register(ProductsImages,ProductsImagesAdmin)

class ProductAttributesAdmin(admin.ModelAdmin):
    list_display=("name","created_date","modify_date")
admin.site.register(ProductAttributes,ProductAttributesAdmin)

class ProductsAttributesValuesAdmin(admin.ModelAdmin):
    list_display=("product_attribute","attribute_value","created_by","created_date","modify_by",
                  "modify_date")
admin.site.register(ProductsAttributesValues,ProductsAttributesValuesAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display=("Firstname","Lastname","email","password","status","created_date","user")
# admin.site.register(User,UserAdmin)

class UserWishListAdmin(admin.ModelAdmin):
    list_display=("user_id","product_id")
admin.site.register(UserWishList,UserWishListAdmin)

class UserAddressAdmin(admin.ModelAdmin):
    list_display=("user_id","address_1","address_2","city","state","country","zipcode")
admin.site.register(UserAddress,UserAddressAdmin) 

class CouponsAdmin(admin.ModelAdmin):
    list_display=("Code","percent","created_by","created_date","modify_by","modify_date","no_of_uses")
admin.site.register(Coupons,CouponsAdmin) 

class CouponsUsedAdmin(admin.ModelAdmin):
    list_display=("user_id","order_id","created_date","coupons_id")
admin.site.register(CouponsUsed,CouponsUsedAdmin) 

class ProductsAsscosAdmin(admin.ModelAdmin):
    list_display=("Product_id","Products_attri_id","Products_value_attri")
admin.site.register(ProductsAsscos,ProductsAsscosAdmin) 

class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display=("name","created_by","created_date","modify_by","modify_date")
admin.site.register(PaymentGateway,PaymentGatewayAdmin) 

class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('user_id','shipping_method','AWB_NO','payment_gateway','transaction_id',
                    'created_date','status','grand_total','shipping_charges','coupon_id',
                    'billing_address_1','billing_address_2','billing_city','billing_state',
                    'billing_country','billing_zipcode','shipping_address_1','shipping_address_2',
                    'shipping_city','shipping_state','shipping_country','shipping_zipcode')
admin.site.register(UserOrder,UserOrderAdmin)

class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order_id','product_id','quantity','amount')
admin.site.register(OrderDetails,OrderDetailsAdmin)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

admin.site.register(CustomUser, CustomUserAdmin)