
from django.urls import path
#from .views import cart_detail, delete_cart, panier_vide, index,detail_product, logine, payment, signup,add_cart,delete_order, valide,admin,responsible,active
from django.contrib.auth.views import LogoutView
from .views import SignUpView,logine,index,cart_detail,add_cart,detail_product,panier_vide,delete_cart,delete_order,payment,valide
urlpatterns = [
    path("",index,name="index"),
    path("signup/" ,  SignUpView . as_view (),  name = "signup" ),
    path("logine/",logine,name="logine"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("product/<str:slug>",detail_product,name="detail"),
    path("product/<str:slug>/add_cart/",add_cart,name="add_cart"),
    path("cart_detail/",cart_detail,name="cart_detail"),
    path("panier_vide/",panier_vide,name="panier_vide"),
    path("cart/delete",delete_cart,name="delete_cart"),
    path("product/<str:slug>/delete_order/",delete_order,name="delete_order"),
    path("payment/",payment,name="payment"),
    path("valide/",valide,name="valide"),
]

