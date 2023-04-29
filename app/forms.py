from .models import User
from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _

class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control'}),validators=[validators.RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')] )
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="confirm password(Again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    name=forms.CharField(max_length=20)
    address=forms.CharField(label="address",widget=forms.Textarea())
    mobile = forms.IntegerField(label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=('name','mobile','address','username','email','password1','password2')

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password=forms.CharField(label=_("password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))
    


