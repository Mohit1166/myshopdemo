
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
# from .models import Banners,Configuration,Cms,Email,Contacts,Category,Products
from custom_admin.models import *
from django.utils.decorators import method_decorator
# from custom_admin.models import Banners



def adminlogin(request):
      """_summary_
       Returns:
          _type_: login.html page
      """
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
      """_summary_

      Returns:
          _type_: starter.html page
      """
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

class Categorys(View):
     
      def get(self,request):
            obj=CategoryForm()
            return render(request,"category_form.html",{'form':obj})


      def post(self,request):
            obj=CategoryForm(request.POST)
            if obj.is_valid():
                  instance=obj.save()
                  instance.created_by=request.user
                  instance.modify_by=request.user
                  instance.save()
                  return redirect('custom_admin:category')
            else:
                  return render(request,"category_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def categorycheck(request):
      obj=Category.objects.all()
      keys={"obj":obj}
      return render(request,"category.html",keys)

class CategoryDelete(View):
      def post(self,request):
            data=request.POST
            id=data.get('id')
            fm=Category.objects.get(id=id)
            fm.delete()
            return redirect('custom_admin:category')

class CategoryEdit(View):
      def get(self,request,id):
            obj=Category.objects.get(id=id)
            fm=CategoryForm(instance=obj)
            return render(request,'category_edit.html',{'form':fm})

      def post(self,request,id):
            cat=Category.objects.get(id=id)
            fm=CategoryForm(request.POST ,instance=cat)
            if fm.is_valid():
                  fm.save()
                  return redirect('custom_admin:category')

# For Product
class Product(View):
     
      def get(self,request):
            
            obj=ProductForm()
            return render(request,"products_form.html",{'form':obj})


      def post(self,request):
            obj=ProductForm(request.POST)
            
            if obj.is_valid():
                  obj.save()
                  return redirect('custom_admin:products')
            else:
                  return render(request,"products_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productscheck(request):
      obj=Products.objects.all()
     
      keys={"obj":obj}
      return render(request,"products.html",keys)

class ProductDelete(View):
      def post(self,request):
            data=request.POST
            id=data.get('id')
            fm=Products.objects.get(id=id)
            fm.delete()
            return redirect('custom_admin:products')

class ProductEdit(View):
      def get(self,request,id):
            obj=Products.objects.get(id=id)
            fm=ProductForm(instance=obj)
            return render(request,'product_edit.html',{'form':fm})

      def post(self,request,id):
            cat=Category.objects.get(id=id)
            fm=CategoryForm(request.POST ,instance=cat)
            if fm.is_valid():
                  fm.save()
                  return redirect('custom_admin:products')



# For ProductCategory
class ProductCategory(View):
     
      def get(self,request):
            obj=ProductCategorys()
            return render(request,"productcateg_form.html",{'form':obj})


      def post(self,request):
            obj=ProductCategorys(request.POST)
            if obj.is_valid():
                  obj.save()
                  return redirect('custom_admin:productscategory')
            else:
                  return render(request,"productcateg_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productscategorycheck(request):
      obj=ProductsCategory.objects.all()
      keys={"obj":obj}
      return render(request,"productcateg.html",keys)

class ProductCategoryDelete(View):
      def post(self,request):
            data=request.POST
            id=data.get('id')
            fm=ProductsCategory.objects.get(id=id)
            fm.delete()
            return redirect('custom_admin:productscategory')

class ProductCategoryEdit(View):
      def get(self,request,id):
            obj=ProductsCategory.objects.get(id=id)
            fm=ProductCategorys(instance=obj)
            return render(request,'productcateg_edit.html',{'form':fm})

      def post(self,request,id):
            cat=ProductsCategory.objects.get(id=id)
            fm=ProductCategorys(request.POST ,instance=cat)
            if fm.is_valid():
                  fm.save()
                  return redirect('custom_admin:productscategory')



# For Product Images
class Productimage(View):
     
      def get(self,request):
            obj=ProductImages()
            return render(request,"productimg_form.html",{'form':obj})


      def post(self,request):
            obj=ProductImages(request.POST)
            if obj.is_valid():
                  obj.save()
                  return redirect('custom_admin:productsimages')
            else:
                  return render(request,"productimg_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productsimagecheck(request):
      obj=ProductsImages.objects.all()
      keys={"obj":obj}
      return render(request,"productimg.html",keys)

class ProductImageDelete(View):
      def post(self,request):
            data=request.POST
            id=data.get('id')
            fm=ProductsImages.objects.get(id=id)
            fm.delete()
            return redirect('custom_admin:productsimages')


class ProductImageEdit(View):
      def get(self,request,id):
            obj=ProductsImages.objects.get(id=id)
            fm=ProductImages(instance=obj)
            return render(request,'productimg_edit.html',{'form':fm})

      def post(self,request,id):
            cat=ProductsImages.objects.get(id=id)
            fm=ProductImages(request.POST ,instance=cat)
            if fm.is_valid():
                  fm.save()
                  return redirect('custom_admin:productsimages')



# For Product Attributes
class ProductAttributes(View):
     
      def get(self,request):
            obj=ProductAttributes
            return render(request,"attributes.html",{'form':obj})


      def post(self,request):
            obj=ProductAttributes(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:productattribute')
            else:
                  return render(request,"attributes_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def attributecheck(request):
      obj=ProductAttributes.objects.all()
      keys={"obj":obj}
      return render(request,"attributes.html",keys)


# For Product Attributes Values
class ProductValues(View):
     
      def get(self,request):
            obj=ProductValues
            return render(request,"productvalues.html",{'form':obj})


      def post(self,request):
            obj=ProductValues(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:productvalue')
            else:
                  return render(request,"productvalues_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productvaluescheck(request):
      obj=ProductsAttributesValues.objects.all()
      keys={"obj":obj}
      return render(request,"productvalues.html",keys)



#  For ProductsAsscos
class ProductsAsscos(View):
     
      def get(self,request):
            obj=ProductsAsscos
            return render(request,"productasscos.html",{'form':obj})


      def post(self,request):
            obj=ProductsAsscos(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:productasscos')
            else:
                  return render(request,"productasscos_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def productasscoscheck(request):
      obj=ProductsAsscos.objects.all()
      keys={"obj":obj}
      return render(request,"productasscos.html",keys)




#  For User
class User(View):
     
      def get(self,request):
            obj=User
            return render(request,"user.html",{'form':obj})


      def post(self,request):
            obj=User(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:user')
            else:
                  return render(request,"user_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def usercheck(request):
      obj=User.objects.all()
      keys={"obj":obj}
      return render(request,"user.html",keys)


#  For UserWishList
class UserWishList(View):
     
      def get(self,request):
            obj=UserWishList
            return render(request,"userlist.html",{'form':obj})


      def post(self,request):
            obj=UserWishList(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:userwishlist')
            else:
                  return render(request,"userlist_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def userlistcheck(request):
      obj=UserWishList.objects.all()
      keys={"obj":obj}
      return render(request,"userlist.html",keys)

# For UserAddress
class UserAddress(View):
     
      def get(self,request):
            obj=UserAddress
            return render(request,"useraddress.html",{'form':obj})


      def post(self,request):
            obj=UserAddress(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:useraddress')
            else:
                  return render(request,"useraddress_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def useraddresscheck(request):
      obj=UserAddress.objects.all()
      keys={"obj":obj}
      return render(request,"useraddress.html",keys)


 #For Coupons
class Coupons(View):
     
      def get(self,request):
            obj=Coupons
            return render(request,"coupons.html",{'form':obj})


      def post(self,request):
            obj=Coupons(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:coupons')
            else:
                  return render(request,"coupons_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def couponscheck(request):
      obj=Coupons.objects.all()
      keys={"obj":obj}
      return render(request,"coupons.html",keys)


#For Coupons-Used
class CouponsUsed(View):
     
      def get(self,request):
            obj=CouponsUsed
            return render(request,"coupons_used.html",{'form':obj})


      def post(self,request):
            obj=CouponsUsed(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:couponsused')
            else:
                  return render(request,"coupons_usedform.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def couponsusedcheck(request):
      obj=CouponsUsed.objects.all()
      keys={"obj":obj}
      return render(request,"coupons_used.html",keys)


#For PaymentGateway
class PaymentGateway(View):
     
      def get(self,request):
            obj=PaymentGateway
            return render(request,"payment.html",{'form':obj})


      def post(self,request):
            obj=PaymentGateway(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:payment')
            else:
                  return render(request,"payment_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def paymentcheck(request):
      obj=PaymentGateway.objects.all()
      keys={"obj":obj}
      return render(request,"payment.html",keys)


#For OrderDetails
class OrderDetails(View):
     
      def get(self,request):
            obj=OrderDetails
            return render(request,"order.html",{'form':obj})


      def post(self,request):
            obj=OrderDetails(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:payment')
            else:
                  return render(request,"order_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def ordercheck(request):
      obj=OrderDetails.objects.all()
      keys={"obj":obj}
      return render(request,"order.html",keys)

#For UserOrder

class UserOrder(View):
     
      def get(self,request):
            obj=UserOrder
            return render(request,"userorder.html",{'form':obj})


      def post(self,request):
            obj=UserOrder(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:userorder')
            else:
                  return render(request,"userorder_form.html",{'form':obj})



@login_required(login_url='/adminpanel/adminlogin', redirect_field_name='adminlogin')
def userordercheck(request):
      obj=UserOrder.objects.all()
      keys={"obj":obj}
      return render(request,"userorder.html",keys)