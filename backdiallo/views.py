
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Product,Cart,Order
from .form import CustomUserCreationForm,LoginForm,PaymentForm
from django.contrib.auth.decorators import login_required

# Page d'accueil
def index(request):
    products = Product.objects.all()
    return render(request,"backdiallo/index.html",{"products":products})
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("logine")
    template_name = "backdiallo/signup.html"

def logine(request):
     logine = LoginForm(request.POST or None)
     if logine.is_valid():
         email = logine.cleaned_data.get("email")
         password = logine.cleaned_data.get("password")
         user = authenticate(request,email=email,password=password)
         if user is not None:
            login(request , user)
            return redirect("index")
     return render(request, "backdiallo/logine.html")



# Fonction Créer et Ajouter n article dans le panier
def add_cart(request, slug):
    # Recupere l'utilisateur
    user = request.user
    # On recupere le produit s'il existe
    product = get_object_or_404(Product, slug=slug)
    # On recupere le panier s'il est existe ,sinon on le créer
    cart, _ = Cart.objects.get_or_create(user=user)
    # On cherche,si on a un article associer à l'utilisateur qui fait 
    # le requete et qui correspond au produit qu'on souhaite ajouter
    order, created = Order.objects.get_or_create(user=user, product=product)                                    
    # Si le produit est créer                                                           
    if created :
        # On l'ajoute dans le panier
        cart.orders.add(order)
        # On sauvegarde le Panier
        cart.save()
    else:
        # Si l'objet n'est pas etais créer et on l'enregistre
        order.quantity += 1
        order.save()
    # On redirige vers la page produit
    return redirect(reverse("detail", kwargs={"slug":slug}))

# Détail d'un produit
def detail_product(request,slug):
    products = get_object_or_404(Product,slug=slug)
    return render(request,"backdiallo/detail.html",{"products":products})

# Afficher le Panier
def cart_detail(request):    
    cart = get_object_or_404(Cart, user=request.user)
    return render(request,"backdiallo/panier.html",{"orders":cart.orders.all()})

# message de panier vide
def panier_vide(request):
    return render(request,"backdiallo/panier_vide.html")

# Supprimer le Panier
def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect("index")

# Supprimer un article dans le panier
def delete_order(request, slug):
    cart = Cart(request)
    cart = get_object_or_404(Product, slug=slug)
    cart.delete()
    return redirect("index")

# message de panier vide
def panier_vide(request):
    return render(request,"backdiallo/panier_vide.html")


# Payement
@login_required(login_url="logine/")
def payment(request):
   if request.method == "POST":
       client = request.user
       email = request.POST['email']
       number = request.POST['number']
       #date_de_commande = request.POST['date_de_commande']
       payer = PaymentForm.objects.create(
           client=client,
           email=email,
           number=number,
           #date_de_commande=date_de_commande,
       )
       payer.save()
       return redirect("valide")
   return render(request,'backdiallo/payment.html')

# valider le payement et message de commande reçu
@login_required(login_url="logine/")
def valide(request):
    user = request.user
    valide = PaymentForm.objects.filter(client=user)
    return render(request,"backdiallo/valide.html",{"valide":valide})
