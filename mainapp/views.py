from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.mail import EmailMessage, get_connection, send_mail
from django.conf import settings


def index(request, message=None):
    cars = Car.objects.all()

    if message:
        return render(request, 'mainapp/index.html', {"cars": cars, "message": message})
    return render(request, 'mainapp/index.html', {"cars": cars})


def show(request, id):
    car = Car.objects.get(id=id)

    return render(request, 'mainapp/show.html', {"car": car})


def rent(request, id):
    return render(request, 'mainapp/rent.html')


def about(request):
    return render(request, 'mainapp/about.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def rentCar(request, id):
    if request.method == 'POST':
        user = User()

        user.agent = request.POST.get('agent')
        user.name = request.POST.get('name')
        user.date_out = request.POST.get('date_out')
        user.time_out = request.POST.get('time_out')
        user.date_in = request.POST.get('date_in')
        user.time_in = request.POST.get('time_in')
        user.fuel = request.POST.get('fuel')
        user.milage = request.POST.get('milage')
        user.notes = request.POST.get('notes')
        user.card_name = request.POST.get('card_name')

        car = Car.objects.get(id=id)
        car.is_free = False
        car.save()
        user.car = car
        user.save()

        SUBJECT = 'Rented a new car'
        text = f'{car.name} car rented'
        send_mail(SUBJECT,
                  text,
                  settings.EMAIL_HOST_USER,
                  [request.POST.get('email')],
                  fail_silently=False)
    return index(request)


def searchCar(request):
    try:
        name = request.POST.get('name')
        car = Car.objects.get(name__iexact=name)
        return show(request, car.id)
    except:
        return index(request, message='Car not found')

