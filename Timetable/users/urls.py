from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    # 事实证明，UID IS NOT INT
    path('<pk>/profile/', views.PersonalDataView.as_view(), name='profile'),
]

