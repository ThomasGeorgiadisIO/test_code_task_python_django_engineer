from django import template
from ..models import Reservation
import itertools

register = template.Library()


@register.filter
def previous_res_id(reservation):

    # A list of reservations of the rental with given reservation ordered by checkin date
    reservation_list = list(Reservation.objects.filter(
        rental_id=reservation.rental_id).order_by('checkin'))
    current_res_index = reservation_list.index(reservation)
    # If current reservation has a previous one is located in the previous index
    # except for the first reservation of the list
    return "--" if current_res_index == 0 else reservation_list[current_res_index-1].pk
