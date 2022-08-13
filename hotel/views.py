from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Hotel, HotelReservation

def hotelsHome(request):

    all_hotels_temp = Hotel.objects.all()
    hotels_temp = Hotel.objects.all()[:4]

    hotels = {}
    all_hotels = {}

    for f in hotels_temp:
        hotels[f.going_to] = f

    for f in all_hotels_temp:
        all_hotels[f.going_to] = f

    hotels = hotels.values()
    all_hotels = all_hotels.values()

    if request.GET.get('check_in'):
        going_to = request.GET.get('going_to')
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        nop = request.GET.get('nop')

        return redirect(f'/hotel/hotels-list/?going_to={going_to}&check_in={check_in}&check_out={check_out}&nop={nop}')

    return render(request, 'hotel/hotel_home.html', context={'all_hotels': all_hotels, 'hotels': hotels})

def hotelsList(request, destination=None):
    all_hotels = Hotel.objects.all()

    if destination:
        hotels = Hotel.objects.filter(going_to__icontains=destination, if_free=True)
    
    else:
        hotels = Hotel.objects.filter(if_free=True)

        if request.GET.get('check_in'):
            going_to = request.GET.get('going_to')
            check_in = request.GET.get('check_in')
            check_out = request.GET.get('check_out')
            nop = request.GET.get('nop')

            hotels = hotels.filter(going_to__icontains=going_to, check_in__lte=check_in, check_out__gte=check_out, number_of_people__gte=nop)

    return render(request, 'hotel/hotel.html', context={'hotels': hotels, 'all_hotels': all_hotels})


def hotelDetail(request, pk):
    hotel = Hotel.objects.get(pk=pk)

    return render(request, 'hotel/hotel_detail.html', context={
        'hotel': hotel,
    })

@login_required(login_url='/account/login/')
def roomReserve(request, pk):
    user = request.user
    hotel = Hotel.objects.get(pk=pk)

    hotel.if_free = False
    hotel.save()

    HotelReservation.objects.create(user=user, hotel=hotel)

    return redirect(f'/hotel/detail/{pk}/')