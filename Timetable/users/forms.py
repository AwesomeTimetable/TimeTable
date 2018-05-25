# https://wsvincent.com/django-allauth-tutorial-custom-user-model/#signup-login-logout
from django import forms
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from string import Template
from django.utils.safestring import mark_safe

from .models import User


class PictureWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        html = Template("""<img src="$link"/>""")
        return mark_safe(html.substitute(link=value))


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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        # TODO: 给我搞清楚这是什么JB玩意
        from django.utils.translation import gettext_lazy as _
        model = User
        # TODO: make clear how to change password.
        # fields = ['username', 'password', 'portrait', 'email']
        fields = ['username', 'portrait', 'email']
        widgets = {
            'password': forms.PasswordInput,
            # 'portrait': PictureWidget,
        }
        # labels = {
        #     'username': _('Writer'),
        # }
        # help_texts = {
        #     'username': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'username': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }
