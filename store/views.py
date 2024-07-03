import json
from django.shortcuts import redirect, render
from store.models import *
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
import razorpay # type: ignore
import requests


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try :
            User.objects.get(username = username)
        except:
            return render(request , "store/login.html" ,{"status" : "User does not exist.."})
        user = authenticate(request , username= username , password = password)
        if user is not None:
            login(request ,user)
            return redirect("store")
        else :
            return render(request , "store/login.html" ,{"status" : "user name or password is incorrect.."})
    return render(request , "store/login.html")


def registerpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request , "store/register.html" , {"status" : "verify password.."})
        try :
            user = User.objects.create_user(username=username , password=password1)
        except:
            return render(request , "store/register.html" , {"status" : "Username already exists.."})
        user.save()
        return redirect("login")
    return render(request , "store/register.html")

@login_required
def logoutuser(request):
    logout(request)
    return redirect("login")

@login_required
def store(request):
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    products = response.json()
    return render(request , "store/store.html" ,{"products" :products})

@login_required
def cart(request):
    user = request.user
    if request.method=="POST":
        data = json.loads(request.body)
        productid = data["productId"]
        action = data["action"]
        url = f"https://fakestoreapi.com/products/{productid}"
        response = requests.get(url)
        product = response.json()
        print(product)

        try:
            item = Cart.objects.get(user = user , product_id= productid)
        except:
            Cart.objects.create(user = user , product_id = productid , price = product['price' ] , image = product["image"]) 
            item = Cart.objects.get(user = user , product_id = productid)
        if action == "add" :
            item.quantity = (item.quantity+1)
            item.quantity_price = item.quantity * item.price
        elif action == "remove":
            item.quantity = (item.quantity-1)
            item.quantity_price = item.quantity * item.price
        item.save()
        if item.quantity<=0:
            item.delete()
    products =  Cart.objects.filter(user=user)
    products_count , total_price =0, 0
    context = {}
    for product in products:
        products_count += product.quantity
        total_price += product.quantity_price

    context["products_count"] = products_count
    context["products"] = products
    context["total_price"] = total_price
    return render(request , "store/cart.html" , context)

@login_required
def checkout(request):
    context = {}
    user = request.user
    products =  Cart.objects.filter(user=user)
    products_count , total_price = 0,0
    for product in products:
        products_count += product.quantity
        total_price += product.quantity_price
    context["products_count"] = products_count
    context["products"] = products
    total_price = round(total_price, 2)
    context["total_price"] = total_price
    if request.method == "GET":
        return render(request , "store/checkout.html" , context)
    if request.method =="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        zipcode = request.POST.get("zipcode")

        try :
            user = Address.objects.get(user = request.user)
            context["flag"] = "Your address is saved already.."
            return render(request , "store/checkout.html" , context)
        except:
            user_address = Address.objects.create(user = request.user,name = name , email = email , Address = address , city = city , state= state , zipcode = zipcode )
            user_address.save()
            context["flag"] = "Address is saved"
            return render(request , "store/checkout.html" , context)
    return render(request , "store/checkout.html" , context)


@login_required
def payments(request):
    products =  Cart.objects.filter(user=request.user)
    total_price = 0
    context = {}
    for product in products:
        total_price += product.quantity_price
    total_price = round(total_price, 2)
    pay_cost = total_price*100
    context["pay_cost"] = pay_cost
    client = razorpay.Client(auth = ("rzp_test_RrmxyExPZGQf8p" , "xT93iTRt2G6J5n13I8KnaQRT"))
    response_payment = client.order.create({'amount':pay_cost, 'currency': 'INR'})
    return render(request , "store/payments.html" , {"order_details" : response_payment})




