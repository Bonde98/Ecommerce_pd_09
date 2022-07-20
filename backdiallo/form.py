from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms


class PaymentForm(forms.Form):
    name = forms.CharField(label="Nom d'utilisateur",
                            widget= forms.TextInput
                            (attrs={"class":"form-control py-3"}))
    email = forms.EmailField(label="Email",
                            widget= forms.EmailInput
                            (attrs={"class":"form-control py-3"}))

    number = forms.IntegerField(label= "Numéro téléphone",
                                 widget= forms.NumberInput
                                 (attrs={"class":"form-control py-3"}))

class LoginForm(forms.Form):
    email = forms.CharField(label = "Email",
                                 widget= forms.TextInput 
                                (attrs={"class":"form-control"}))
                                
    password = forms.CharField(label = "Mot de passe",
                                widget= forms.PasswordInput
                                (attrs={"class":"form-control"}))
class CustomUserCreationForm(UserCreationForm):
     email = forms.EmailField(label = "Email",
                                        widget= forms.EmailInput 
                                        (attrs={"class":"form-control py-3"})) 
     username = forms.CharField(label = "Nom d'utilisateur",
                                        widget= forms.TextInput 
                                        (attrs={"class":"form-control py-3",}))        
     password1 = forms.CharField(label = "Mot de passe",
                                        widget= forms.PasswordInput
                                        (attrs={"class":"form-control py-3"}))
     password2 = forms.CharField(label = "Confirmer Mot de passe",
                                        widget= forms.PasswordInput
                                        (attrs={"class":"form-control py-3"}))                            
     class Meta:
        model = CustomUser
        fields = ('email','username','password1','password2',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
