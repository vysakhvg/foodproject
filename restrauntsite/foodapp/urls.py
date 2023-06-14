from . import views
from django.urls import path

urlpatterns = [
    path('', views.demo, name='demo'),
    path('restaurant', views.restaurant, name='restaurant'),
    path('restauranthr', views.restauranthri, name='restaurant1'),
    path('restaurantri', views.restauranttriva, name='restaurant2'),
    path('booking', views.booking, name='booking'),
    path('restaurant/<int:restaurant_id>/', views.detail, name='details'),
    path('thank', views.thank, name='thank'),
    path('restaurant/<int:restaurant_id>/', views.detail1, name='detail1'),
    path('restaurant/<int:restaurant_id>/', views.detail2, name='detail2'),
    path('foodorder', views.foodorder, name='foodorder'),
]
