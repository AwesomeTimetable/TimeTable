from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages

from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer
from .forms import CustomUserCreationForm, UserUpdateForm, UserLogin, UserRegister


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


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


class PersonalDataView(generic.DetailView):
    """
    个人信息对应的VIEW
    TODO:期望是个人信息对应要加上默认
    """
    model = User
    template_name = 'users/profile.html'
    # 现在对应的user
    context_object_name = 'current_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user: User = context['current_user']
        user_form = UserUpdateForm(initial={
            'email': user.email,
            'username': user.username,
            'portrait': user.portrait,
            'password': user.password
        })

        user_form.email = user.email
        user_form.username = user.username
        user_form.portrait = user.portrait
        context['form'] = user_form
        return context

