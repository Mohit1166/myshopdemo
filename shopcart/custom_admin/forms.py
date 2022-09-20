from dataclasses import field
from django import forms
from custom_admin.models import *

class BannersForm(forms.ModelForm):  
    class Meta:  
        model = Banners  
        fields = "__all__"  #("name","roll","city")
        
class ConfigForm(forms.ModelForm):  
    class Meta:  
        model =  Configuration
        fields = "__all__"

class CMSForm(forms.ModelForm):  
    class Meta:  
        model =  Cms
        fields = "__all__"

class EmailsForm(forms.ModelForm):  
    class Meta:  
        model =  Email
        fields = "__all__"

class ContactsForm(forms.ModelForm):  
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

class ProductCategorysForm(forms.ModelForm):  
    class Meta:  
        model =ProductsCategory
        fields = "__all__"

class ProductImagesForm(forms.ModelForm):  
    class Meta:  
        model =ProductsImages
        fields = "__all__"

class ProductAttributesForm(forms.ModelForm):  
    class Meta:  
        model =ProductAttributes
        fields = "__all__"

class ProductValuesForm(forms.ModelForm):  
    class Meta:  
        model =ProductsAttributesValues
        fields = "__all__"

class ProductsAsscosForm(forms.ModelForm):  
    class Meta:  
        model =ProductsAsscos
        fields = "__all__"

class UserForm(forms.ModelForm):  
    class Meta:  
        model =User
        fields = "__all__"

class UserWishListForm(forms.ModelForm):  
    class Meta:  
        model =UserWishList
        fields = "__all__"

class UserAddressForm(forms.ModelForm):  
    class Meta:  
        model =UserAddress
        fields = "__all__"

class CouponsForm(forms.ModelForm):  
    class Meta:  
        model =Coupons
        fields = "__all__"

class CouponsUsedForm(forms.ModelForm):  
    class Meta:  
        model =CouponsUsed
        fields = "__all__"

class PaymentGatewayForm(forms.ModelForm):  
    class Meta:  
        model =PaymentGateway
        fields = "__all__"

class OrderDetailsForm(forms.ModelForm):  
    class Meta:  
        model =OrderDetails
        fields = "__all__"

class UserOrderForm(forms.ModelForm):  
    class Meta:  
        model =UserOrder
        fields = "__all__"

