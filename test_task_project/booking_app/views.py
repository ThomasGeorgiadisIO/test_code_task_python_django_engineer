from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class ReservationList(ListView):
    model = Reservation
    template_name = "booking_app/reservation_list.html"
