
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
from .models import Banners
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


class BannersIndex(View):

      # login_url = '/adminpanel/adminlogin'
      # redirect_field_name = 'admin_login'

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


      
# @login_required(login_url='adminpanel/adminlogin', redirect_field_name='admin_login')
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

