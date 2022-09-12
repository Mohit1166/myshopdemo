
from statistics import fmean
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required,permission_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from custom_admin.forms import *
from .models import Banners,Configuration,Cms,Email,Contacts,Category,Products
from django.utils.decorators import method_decorator
# from custom_admin.models import Banners



def adminlogin(request):
      if request.user.is_authenticated:
            return redirect("/adminpanel/")

      if request.method=="POST":
            username=request.POST["Username"]
            password=request.POST["Password"]
            if username and password:
                  user=authenticate(username=username, password=password)
                  # print(user)
                  if user is not None:
                        # print(user)
                        login(request, user)
                        return redirect('custom_admin:start')
                  else:
                        messages.error(request, 'Please enter correct credentials')
            else:
                  messages.error(request,"Check out some error")
      return render(request,"login.html")

@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='admin_login')
def start(request):
      return render(request,"starter.html")

def admin_logout(request):
      logout(request)
      return render(request,'login.html')

#crud operations

# def banners_index(request):
#       obj=bannersForm()
#       return render(request,"banners_click.html",{'form':obj})

'''For Banners'''
class BannersIndex(View):
      # @method_decorator(login_required)
      def get(self,request):
            obj=BannersForm()
            return render(request,"banners_click.html",{'form':obj})

      # @method_decorator(login_required)
      def post(self,request):
            obj=BannersForm(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:banners')
            else:
                  return render(request,"banners_click.html",{'form':obj})


      
@login_required(login_url='adminpanel/adminlogin', redirect_field_name='admin_login')
def check(request):
      return render(request,"banners.html")

# def banners_view(request):
#       check=Banners.objects.all()
#       return render(request,"banners.html",{'object':check})

@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def bannerscheck(request):
      obj=Banners.objects.all()
      keys={"obj":obj}
      return render(request,"banners.html",keys)
      
#For banner Delete
class Delete(View):
      def post(self,request):
            data=request.POST
            id=data.get('id')
            fm=Banners.objects.get(id=id)
            fm.delete()
            return redirect('custom_admin:banners')
#For banner Edit
class Edit(View):
    
      def get (self,request,id):
            obj=Banners.objects.get(id=id)
            fm=BannersForm(instance=obj)
            return render(request,"edit.html",{'form':fm})

      def post(self,request, id):
        ban = Banners.objects.get(id=id)
        fm = BannersForm(request.POST,request.FILES,instance=ban)
        if fm.is_valid():
            fm.save()
            return redirect('custom_admin:banners')

#For configuration
class Configuration(View):
     
      def get(self,request):
            obj=Config()
            return render(request,"config.html",{'form':obj})


      def post(self,request):
            obj=Config(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:config')
            else:
                  return render(request,"config_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def configurationcheck(request):
      obj=Configuration.objects.all()
      keys={"obj":obj}
      return render(request,"config.html",keys)

#For CMS
class CMS(View):
     
      def get(self,request):
            obj=CMS
            return render(request,"cms.html",{'form':obj})


      def post(self,request):
            obj=CMS(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:cms')
            else:
                  return render(request,"cms_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def cmscheck(request):
      obj=Cms.objects.all()
      keys={"obj":obj}
      return render(request,"cms.html",keys)

#For Emails
class Email(View):
     
      def get(self,request):
            obj=Emails
            return render(request,"email.html",{'form':obj})


      def post(self,request):
            obj=Emails(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:email')
            else:
                  return render(request,"email_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def emailcheck(request):
      obj=Email.objects.all()
      keys={"obj":obj}
      return render(request,"email.html",keys)

#For contacts
class Contacts(View):
     
      def get(self,request):
            obj=Contacts
            return render(request,"contacts.html",{'form':obj})


      def post(self,request):
            obj=Contacts(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:contacts')
            else:
                  return render(request,"contacts_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def contactscheck(request):
      obj=Contacts.objects.all()
      keys={"obj":obj}
      return render(request,"contacts.html",keys)

#For Category

class Category(View):
     
      def get(self,request):
            obj=CategoryForm
            return render(request,"category.html",{'form':obj})


      def post(self,request):
            obj=CategoryForm(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:category')
            else:
                  return render(request,"category_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def categorycheck(request):
      obj=Category.objects.all()
      keys={"obj":obj}
      return render(request,"category.html",keys)

# For Product
class Product(View):
     
      def get(self,request):
            obj=ProductForm
            return render(request,"products.html",{'form':obj})


      def post(self,request):
            obj=ProductForm(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:products')
            else:
                  return render(request,"products_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productscheck(request):
      obj=Products.objects.all()
      keys={"obj":obj}
      return render(request,"products.html",keys)


# For ProductCategory
class ProductCategory(View):
     
      def get(self,request):
            obj=ProductCategory
            return render(request,"productcateg.html",{'form':obj})


      def post(self,request):
            obj=ProductCategory(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:productscategories')
            else:
                  return render(request,"productcateg_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productscategorycheck(request):
      obj=ProductCategory.objects.all()
      keys={"obj":obj}
      return render(request,"productcateg.html",keys)



# For Product Images
class ProductImages(View):
     
      def get(self,request):
            obj=ProductImages
            return render(request,"productcateg.html",{'form':obj})


      def post(self,request):
            obj=ProductImages(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:productscategories')
            else:
                  return render(request,"productcateg_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productscategorycheck(request):
      obj=ProductImages.objects.all()
      keys={"obj":obj}
      return render(request,"productcateg.html",keys)