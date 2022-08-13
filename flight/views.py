import datetime

from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from .models import Flight, FlightReservation

def index(request):
    flights_temp = Flight.objects.all()[:4]
    all_flights_temp = Flight.objects.all()

    flights = {}
    all_flights = {}

    for f in flights_temp:
        flights[f.to_location] = f

    for f in all_flights_temp:
        all_flights[f.to_location] = f

    flights = flights.values()
    all_flights = all_flights.values()

    if request.method == 'GET' and request.GET.get('from') is not None:
        from_loc = request.GET.get('from')
        to = request.GET.get('to')
        departing = request.GET.get('departing')
        returning = request.GET.get('returning') or None
        nop = request.GET.get('nop')

        return redirect(f'/flight/{to}/?from={from_loc}&to={to}&departing={departing}&returning={returning}&nop={nop}')

    return render(request, 'flight/index.html', context={
        'flights': flights,
        'all_flights': all_flights,
    })

def flightDestination(request, destination):
    to = None
    from_loc = None

    all_flights = Flight.objects.all()
    flights = None

    if request.GET.get('from'):
        from_loc = request.GET.get('from')
        to = request.GET.get('to')
        departing = request.GET.get('departing')
        returning = request.GET.get('returning') or None
        nop = request.GET.get('nop')

        if returning == 'None':
            returning = None

        if returning is not None:
            flights = Flight.objects.filter(from_location__icontains=from_loc, to_location__icontains=to, date__lte=departing, returning_date__gte=returning, max_passengers__gte=nop)
        else:
            flights = Flight.objects.filter(from_location__icontains=from_loc, to_location__icontains=to, date__lte=departing, max_passengers__gte=nop)
    
    else:
        flights = Flight.objects.filter(to_location__icontains=destination)
        to = destination

    if not flights.exists():
            return redirect('/flight/not-found/')

    return render(request, 'flight/flight_list.html', context={'flights': flights, 'all_flights': all_flights, 'from_loc': from_loc, 'to': to})


def contact(request):
    return render(request, 'flight/contact_us.html', context={})


def flightDetail(request, pk):
    flight = Flight.objects.get(pk=pk)

    return render(request, 'flight/flight_detail.html', context={
        'flight': flight,
    })

@login_required(login_url='/account/login/')
def flightReserve(request, pk):
    user = request.user
    flight = Flight.objects.get(pk=pk)

    FlightReservation.objects.create(user=user, flight=flight)

    return redirect(f'/flight/{pk}/detail/')


def flight_404(request):
    return render(request, 'flight/notfound.html', context={})