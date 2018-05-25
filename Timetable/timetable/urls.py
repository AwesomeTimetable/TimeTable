from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('deadlines/', views.index, name='deadlines'),
    path('deadlines/', views.DeadlinesView.as_view(), name='deadlines'),
    # path('<int:pk>/deadline/', views.DeadlinesView.as_view(), name='detail-deadline'),
]

