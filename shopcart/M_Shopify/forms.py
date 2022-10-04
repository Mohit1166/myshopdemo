from django import forms
from django.contrib.auth import get_user_model
from custom_admin.models import CustomUser
from django.core.exceptions import ValidationError
User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField( min_length=5, max_length=150)  
    email = forms.EmailField()  
    mobile=forms.CharField(max_length=13)
    password = forms.CharField( widget=forms.PasswordInput())  
    confirmpassword = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = CustomUser
        fields = ('username','email','mobile','password','confirmpassword')


    def clean_username(self):
        username = self.cleaned_data['username'].lower()   
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username 
       

    def clean_email(self):
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email 
    
    def clean_mobile(self):
        valname=self.cleaned_data['mobile']
        if len(valname)<10:
            raise forms.ValidationError("The length of the mobile_number should be more than 10")
        return valname
    
    def clean_confirmpassword(self):
        password_1=self.cleaned_data['password']
        password_2=self.cleaned_data['confirmpassword']
        if password_1!=password_2:
            raise ValidationError("Password don't match")  
        return password_2

    def save(self,commit=True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],
            self.cleaned_data['email'], 
            self.cleaned_data['mobile'], 
            self.cleaned_data['password']  
        )  
        return user 


 
    
    