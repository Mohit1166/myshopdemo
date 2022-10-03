from django.shortcuts import render
from .forms import UserRegisterForm
from django.views import View
from django.shortcuts import render, redirect

# Create your views here.

def main(request):
    return render(request,"myuser.html")

# def registration(request):
#     if request.method== "POST":
#         form=UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(user.password)
#             user.save()
#         else:
#             print(form.errors)
#     else:
#         form=UserRegisterForm()
#     return render (request,"forlogin/mylogin.html",{"form":form})

class registration(View):
    def get(self,request): 
        obj=UserRegisterForm()
        return render (request,"forlogin/mylogin.html",{"form":obj})

    def post(self,request):
        obj=UserRegisterForm(request.POST)
        if obj.is_valid():
            obj.save()    
        else:
            print(obj.errors)
            return render (request,"forlogin/mylogin.html",{"form":obj})


