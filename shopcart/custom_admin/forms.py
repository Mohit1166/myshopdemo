from django import forms
from custom_admin.models import *

class BannersForm(forms.ModelForm):  
    class Meta:  
        model = Banners  
        fields = "__all__"
        
