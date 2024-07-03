from django.urls import path
from store.views import *


urlpatterns = [
    path("",loginpage , name="login"),
    path("store/" , store , name ="store"),
    path("register/" , registerpage , name="register"),
    path("logout/" , logoutuser , name ="logout"),
    path("cart/" , cart , name ="cart"),
    path("checkout/" , checkout , name="checkout"),
    path("payments/" , payments , name ="payments")
] 