from dataclasses import field
from django import forms
from custom_admin.models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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
        fields= ['name','sku','short_description','long_description','modify_status','price','quantity','meta_title','meta_desc','meta_keywords','is_featured']
        # fields="__all__"
       
class ProductCategorysForm(forms.ModelForm):  
    class Meta:  
        model =ProductsCategory
        fields = "__all__"

class ProductImagesForm(forms.ModelForm):  
    class Meta:  
        model =ProductsImages
        fields = ["image"]

class ProductAttributesForm(forms.ModelForm):  
    class Meta:  
        model =ProductAttributes
        fields = ["name"]

class ProductValuesForm(forms.ModelForm):  
    class Meta:  
        model =ProductsAttributesValues
        fields = "__all__"

class ProductsAsscosForm(forms.ModelForm):  
    class Meta:  
        model =ProductsAsscos
        fields = ["Products_attri_id", "Products_value_attri_id"]
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['Products_value_attri_id'].queryset = ProductsAttributesValues.objects.none()
            if 'Products_attri_id' in self.data:
                try:
                    product_attribute_id = int(self.data.get('Products_attri_id'))
                    self.fields['Products_value_attri_id'].queryset = ProductsAttributesValues.objects.filter(product_attribute_id=product_attribute_id).order_by('name')
                except (ValueError, TypeError):
                    pass 
            elif self.instance.pk:
                self.fields['Products_value_attri_id'].queryset = self.instance.Products_value_attri_id_set.order_by('name')

# class UserForm(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"

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

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")