from django import forms
from custom_admin.models import *

class BannersForm(forms.ModelForm):  
    class Meta:  
        model = Banners  
        fields = "__all__"
        
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
        fields = "__all__"

class ProductForm(forms.ModelForm):  
    class Meta:  
        model =Products
        fields = "__all__"

class ProductCategory(forms.ModelForm):  
    class Meta:  
        model =ProductsCategory
        fields = "__all__"

class ProductImages(forms.ModelForm):  
    class Meta:  
        model =ProductsImages
        fields = "__all__"

class ProductAttributes(forms.ModelForm):  
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

# class User(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"

# class User(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"

# class User(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"

# class User(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"

# class User(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"

# class User(forms.ModelForm):  
#     class Meta:  
#         model =User
#         fields = "__all__"