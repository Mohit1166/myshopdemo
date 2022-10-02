from django.shortcuts import render
from .forms import UserRegisterForm


# Create your views here.

def main(request):
    return render(request,"myuser.html")

def registration(request):
    if request.method== "POST":
        form=UserRegisterForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        else:
            print(form.errors)
    else:
        form=UserRegisterForm()
    return render (request,"forlogin/mylogin.html",{"form":form})
