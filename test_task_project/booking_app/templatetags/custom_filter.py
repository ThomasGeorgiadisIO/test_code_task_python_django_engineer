from django import template
from ..models import Reservation
import itertools

register = template.Library()

@register.filter
def previous_res_id(reservation):

    # A list of reservations of the rental with given reservation

    reservation_list = Reservation.objects.filter(rental_id=reservation.rental_id).order_by('checkin')

    # Pair current reservation with the previous

    def pair(iterable):
        previous_res, current_res = itertools.tee(iterable)
        next(current_res, None)
        return zip(previous_res, current_res)

    # Locate previous reservation of the given reservation

    for previous_res, current_res in pair(reservation_list):
        if current_res == reservation:
            return previous_res.pk

