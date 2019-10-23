from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(label='Correo', max_length=254, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(label='Nombres',max_length=100, required=True, widget=forms.TextInput())
    last_name = forms.CharField(label='Apellidos',max_length=100, required=True, widget=forms.TextInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ChangeUserForm(UserChangeForm):
    email = forms.CharField(label='Correo', max_length=254, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(label='Nombres',max_length=100, required=True, widget=forms.TextInput())
    last_name = forms.CharField(label='Apellidos',max_length=100, required=True, widget=forms.TextInput())
    password = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

#class ChangePassword(SetPasswordForm):
#    username =  None
#    email = None
#    class Meta:
#        model = User
#        fields = ('username', 'email', 'password1', 'password2')