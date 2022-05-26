from django import template

register = template.Library()


class ReservationFilter():
    @register.filter
    def previous_reservation_pk_filter(object_list):
        for idx, object in enumerate(object_list):
            if idx == 0 or object_list[idx-1].rental_id != object.rental_id:
                object.previous_reservation_pk = "--"
                continue
            if object_list[idx-1].rental_id == object.rental_id:
                object.previous_reservation_pk = object_list[idx-1].pk
        return object_list
