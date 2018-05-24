# https://wsvincent.com/django-allauth-tutorial-custom-user-model/#signup-login-logout
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields


class UserRegister(forms.Form):
    username = forms.CharField(label='注册用户名', max_length=100)
    password1 = forms.CharField(label='设置密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='电子邮件')
    phone_number = forms.CharField(label='手机号码', max_length=15)


class UserLogin(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
