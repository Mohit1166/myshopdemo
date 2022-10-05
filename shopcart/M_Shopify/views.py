from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from custom_admin.models import *
from django.http import JsonResponse


# Create your views here.

def main(request):
    return render(request, "myuser.html")


class registration(View):
    def get(self, request):
        obj = UserRegisterForm()
        return render(request, "forlogin/mylogin.html", {"form": obj})

    def post(self, request):
        obj = UserRegisterForm(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('M_Shopify:homepage')
        else:
            print(obj.errors)
            return render(request, "forlogin/mylogin.html", {"form": obj})


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
                return redirect('M_Shopify:homepage')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "forlogin/mylogin.html", {"form": form})


@login_required(login_url="/mylogin", redirect_field_name="mylogin")
def home_page(request):
    products = Products.objects.all()
    return render(request, "home/home.html", {'obj': products})


def user_logout(request):
    logout(request)
    return redirect('M_Shopify:mylogin')


def add_cart(request):
    cart_product = {}
    cart_product[str(request.GET['id'])] = {
        'title': request.GET['title'],
        'qty': request.GET['qty'],
    }
    if 'cartdata' in request.session:
        if str(request.GET['id']) in request.session['cartdata']:
            cart_data = request.session['cartdata']
            cart_data[str(request.GET['id'])]['qty'] = int(
                cart_product[str(request.GET['id'])]['qty'])
            cart_data.update(cart_data)
            request.session['cartdata'] = cart_data

        else:
            cart_data = request.session['cartdata']
            cart_data.update(cart_product)
            request.session['cartdata']=cart_data
    else:
        request.session[cart_data]=cart_product
    return JsonResponse({'data': request.session['cartdata'],'totalitems': len(request.session['cartdata'])})
