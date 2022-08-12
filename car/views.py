from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Car, CarReservation

def carsHome(request):
    all_cars = Car.objects.all()

    if request.GET.get('pick_up_date'):
        pick_up_location = request.GET.get('pick_up_location')
        pick_up_date = request.GET.get('pick_up_date')
        drop_off_date = request.GET.get('drop_off_date')
        pick_up_time = request.GET.get('pick_up_time')
        drop_off_time = request.GET.get('drop_off_time')
        
        return redirect(f'/car/cars-list/?pick_up_location={pick_up_location}&pick_up_date={pick_up_date}&drop_off_date={drop_off_date}&pick_up_time={pick_up_time}&drop_off_time={drop_off_time}')

    return render(request, 'car/car_home.html', context={'all_cars': all_cars})

def carsList(request, location=None):

    all_cars = Car.objects.all()

    if location:
        cars = Car.objects.filter(location__icontains=location)
    
    else:
        if request.GET.get('pick_up_date'):
            pick_up_location = request.GET.get('pick_up_location')
            pick_up_date = request.GET.get('pick_up_date')
            drop_off_date = request.GET.get('drop_off_date')
            pick_up_time = request.GET.get('pick_up_time')
            drop_off_time = request.GET.get('drop_off_time')

            cars = Car.objects.filter(location__icontains=pick_up_location, pick_up_date__lte=pick_up_date, drop_off_date__gte=drop_off_date, pick_up_time__lte=pick_up_time, drop_off_time__gte=drop_off_time)

        else:
            cars = Car.objects.all()

    return render(request, 'car/car.html', context={'cars': cars, 'all_cars': all_cars})


def carDetail(request, pk):
    car = Car.objects.get(pk=pk)

    return render(request, 'car/car_detail.html', context={
        'car': car,
    })

@login_required(login_url='/account/login/')
def carReserve(request, pk):
    user = request.user
    car = Car.objects.get(pk=pk)

    CarReservation.objects.create(user=user, car=car)

    return redirect(f'/car/detail/{pk}/')