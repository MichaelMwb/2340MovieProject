from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('signup/', views.signup, name='accounts.signup'),
    path('orders/', views.orders, name='accounts.orders'),
    path('forgot_password/', views.forgot_password, name='accounts.forgot_password'),
]
