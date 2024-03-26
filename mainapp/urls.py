from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('show/<int:id>/', show, name='show'),
    path('rent/<int:id>/', rent, name='rent'),
    path('rentCar/<int:id>/', rentCar, name='rentCar'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', searchCar, name='search'),
]
