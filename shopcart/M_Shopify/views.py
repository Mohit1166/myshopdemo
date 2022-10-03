from django.shortcuts import render
from .forms import UserRegisterForm
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import messages



# Create your views here.

def main(request):
    return render(request,"myuser.html")

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



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('M_Shopify:index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request,"forlogin/mylogin.html", {"form":form})

def home_page(request):
    return render(request,"home/home.html")
