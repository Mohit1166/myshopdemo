from dataclasses import field
from django import forms
from custom_admin.models import *

class BannersForm(forms.ModelForm):  
    class Meta:  
        model = Banners  
        fields = "__all__"  #("name","roll","city")
        
class Config(forms.ModelForm):  
    class Meta:  
        model =  Configuration
        fields = "__all__"

class CMS(forms.ModelForm):  
    class Meta:  
        model =  Cms
        fields = "__all__"

class Emails(forms.ModelForm):  
    class Meta:  
        model =  Email
        fields = "__all__"

class Contacts(forms.ModelForm):  
    class Meta:  
        model =  Contacts
        fields = "__all__"

class CategoryForm(forms.ModelForm):  
    class Meta:  
        model =Category
        fields =("name","modify_status","parent_id")

class ProductForm(forms.ModelForm):  
    class Meta:  
        model =Products
        fields= "__all__"
        # fields = ("name","sku","short_description","long_description","price","special_price","from_special_price",
        # "modify_status","quantity","meta_title","meta_desc","meta_keywords","is_featured,")

class ProductCategorys(forms.ModelForm):  
    class Meta:  
        model =ProductsCategory
        fields = "__all__"

class ProductImages(forms.ModelForm):  
    class Meta:  
        model =ProductsImages
        fields = "__all__"

class Productattributes(forms.ModelForm):  
    class Meta:  
        model =ProductAttributes
        fields = "__all__"

class ProductValues(forms.ModelForm):  
    class Meta:  
        model =ProductsAttributesValues
        fields = "__all__"

class ProductsAsscos(forms.ModelForm):  
    class Meta:  
        model =ProductsAsscos
        fields = "__all__"

class User(forms.ModelForm):  
    class Meta:  
        model =User
        fields = "__all__"

class UserWishList(forms.ModelForm):  
    class Meta:  
        model =UserWishList
        fields = "__all__"

class UserAddress(forms.ModelForm):  
    class Meta:  
        model =UserAddress
        fields = "__all__"

class Coupons(forms.ModelForm):  
    class Meta:  
        model =Coupons
        fields = "__all__"

class CouponsUsed(forms.ModelForm):  
    class Meta:  
        model =CouponsUsed
        fields = "__all__"

class PaymentGateway(forms.ModelForm):  
    class Meta:  
        model =PaymentGateway
        fields = "__all__"

class OrderDetails(forms.ModelForm):  
    class Meta:  
        model =OrderDetails
        fields = "__all__"

class UserOrder(forms.ModelForm):  
    class Meta:  
        model =UserOrder
        fields = "__all__"

