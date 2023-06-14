from django.contrib import admin

from .models import Todaysspecial, Drinks, starters, Deserts, Maindishes
from .models import District, Restaurant, restaurantfooderna, restaurantfoodthris, restaurantfoodtrivan

# Register your models here.

admin.site.register(Todaysspecial)
admin.site.register(starters)
admin.site.register(Maindishes)
admin.site.register(Deserts)
admin.site.register(Drinks)


class Districtadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(District, Districtadmin)


class Restaurantadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Restaurant, Restaurantadmin)


class Foodadminerna(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(restaurantfooderna, Foodadminerna)


class Foodadminthri(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(restaurantfoodthris, Foodadminthri)


class Foodadmintriv(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 20


admin.site.register(restaurantfoodtrivan, Foodadmintriv)
