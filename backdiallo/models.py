from django.db import models
#from django.contrib.auth.models import User

#from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
#Class Model utilisateur
class CustomUser(AbstractUser):
     username = None
     email = models.EmailField(('email address'), unique=True)
     is_admin = models.BooleanField(default=False)
     is_responsible = models.BooleanField(default=False)
     is_active = models.BooleanField(default=True)


     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = []

     objects = CustomUserManager()

     def __str__(self):
        return self.email

# Class Produit
class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products",blank=True,null=True)

    def __str__(self):
        return f"{self.name} {self.price}"

"""
# class Article(order)
- utilistateur
- Produit
- Quantité
- Commandé ou non
"""
class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.product.name} {self.quantity}"

"""
# Class Panier(Cart)
- Utilisateur
- Articles
- Commande ou non 
- Date de la commande

"""
class Cart(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)

    def  __str__(self):
        return f"{self.user.email}"

"""
# Class payement
-Client
- Quantité
-email
-numéro téléphone
-date de commande
"""
class Payment(models.Model):
    client = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    email = models.EmailField()
    number = models.CharField(max_length=9)
    date_de_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.client} {self.email}"

