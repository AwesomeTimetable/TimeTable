from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout, authenticate
from django.views import generic
from django.contrib import messages

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from .forms import CustomUserCreationForm, UserChangeForm, UserCreationForm, UserLogin, UserRegister


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrives user accounts
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class UserCreateViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


def user_login(request):
    if request.method == "POST":
        print('POST 的表单站立在大地上')
        login_form = UserLogin(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                '''用户登陆后，Django会自动调用默认的session应用，
                    将用户的id存至session中，通常情况下，login与authenticate
                    配合使用'''
                login(request, user)
                return redirect('index')
            else:
                # 登陆失败
                return redirect('login')
        else:
            return redirect('login')

    if request.method == "GET":
        login_form = UserLogin()
        return render(request, 'users/login.html', {"forms": login_form})


def user_register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        f = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': f})


class SignUp(generic.CreateView):
    pass

