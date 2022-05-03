from django.urls import path
from .views import ChangePasswordView, UserUpdateView

urlpatterns =[
    path('password-change', ChangePasswordView.as_view(), name='password_change'),
    path('<pk>/update', UserUpdateView.as_view(), name='profile'),
    ]