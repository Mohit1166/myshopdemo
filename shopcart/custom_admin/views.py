
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from custom_admin.forms import *
from .models import Banners
# from custom_admin.models import Banners

# from shopcart.custom_admin.forms import BannersForm
# Create your views here.
# @login_required(login_url='adminpanel/adminlogin', redirect_field_name='adminlogin')
# def start(request):
#       return render(request,"starter.html")


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

@login_required(login_url='adminpanel/adminlogin', redirect_field_name='admin_login')
def start(request):
      return render(request,"starter.html")

def admin_logout(request):
      logout(request)
      return render(request,'login.html')

#crud operations

# def banners_index(request):
#       obj=bannersForm()
#       return render(request,"banners_click.html",{'form':obj})


class banners_index(View):
      def get(self,request):
            obj=bannersForm()
            return render(request,"banners_click.html",{'form':obj})

      def post(self,request):
            obj=bannersForm(request.POST,request.FILES)
            if obj.is_valid():
                  instance=obj.save()
                  print(instance.banner_path.path)
                 
                  return redirect('custom_admin:banners')
            else:
                  return render(request,"banners_click.html",{'form':obj})


      
# @login_required(login_url='adminpanel/adminlogin', redirect_field_name='admin_login')
def check(request):
      return render(request,"banners.html")

# def banners_view(request):
#       check=Banners.objects.all()
#       return render(request,"banners.html",{'object':check})

# @login_required(login_url='adminpanel/adminlogin', redirect_field_name='admin_login')
def banners_check(request):
      obj=Banners.objects.all()
      keys={"obj":obj}
      return render(request,"banners.html",keys)

# def banners_click(request):
#       if request.method=="POST":
#             form=Banners()
#             if len(request.FILES)!=0:
#                   form.banner_path=request.FILES["image"]
#             form.save()
#             return redirect("/")
#       return render (request,"banners_click.html")

# def banner_image(request):
#       if request=="POST":
#             form=bannersForm(request.POST,request.FILES)

#             if form.is_valid():
#                   form.save()
#                   return redirect("custom_admin:start")