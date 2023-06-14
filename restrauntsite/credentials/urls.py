from . import views
from django.urls import path

urlpatterns = [
    path('Signup', views.Signup, name='Signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
