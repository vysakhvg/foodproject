from django.shortcuts import render
from .models import Todaysspecial, starters, Maindishes, Deserts, Drinks
from .models import Restaurant, restaurantfooderna, restaurantfoodthris, restaurantfoodtrivan


# Create your views here.
def demo(request):
    obj = Todaysspecial.objects.all()
    sta = starters.objects.all()
    main = Maindishes.objects.all()
    des = Deserts.objects.all()
    dri = Drinks.objects.all()
    return render(request, 'index.html', {'data': obj, 'start': sta, 'main': main, 'desert': des, 'drinks': dri})


def restaurant(request):
    res = Restaurant.objects.all()
    diserna = restaurantfooderna.objects.all()
    return render(request, 'restaurant.html', {'restaurant': res, 'dishes': diserna})


def restauranthri(request):
    disthri = restaurantfoodthris.objects.all()
    return render(request, 'restauranthri.html', {'dishes': disthri})


def restauranttriva(request):
    distriv = restaurantfoodtrivan.objects.all()
    return render(request, 'restauranttrivan.html', {'dishes': distriv})


def booking(request):
    return render(request, 'booking.html')


def thank(request):
    return render(request, 'thank.html')


def foodorder(request):
    return render(request, 'foodorder.html')


def booking(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        quantity = request.POST.get("quantity")
        phone = request.POST.get("phone")
        date = request.POST.get("date-picker")
        customer = booking(name=name, quantity=quantity, phone=phone)
        customer.save()
    return render(request, 'booking.html')


def detail(request, restaurant_id):
    diserna = restaurantfooderna.objects.get(id=restaurant_id)
    return render(request, 'details1.html', {'dishes': diserna})


def detail1(request, restaurant_id):
    disthri = restaurantfoodthris.objects.get(id=restaurant_id)
    return render(request, 'details.2.html', {'dishes': disthri})


def detail2(request, restaurant_id):
    distriv = restaurantfoodtrivan.objects.get(id=restaurant_id)
    return render(request, 'details3.html', {'dishes': distriv})
