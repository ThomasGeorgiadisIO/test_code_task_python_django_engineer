from django.views.generic import ListView
from .models import Reservation


class ReservationList(ListView):
    model = Reservation
    template_name = "booking_app/reservation_list.html"
    ordering = ['rental_id', 'checkin']