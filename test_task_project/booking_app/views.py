from django.views.generic import ListView
from .models import Reservation
from django.db.models import OuterRef, Subquery


class ReservationList(ListView):
    model = Reservation
    template_name = "booking_app/reservation_list.html"

    def get_queryset(self):
        '''overriding queryset to annotate the previous reservation id'''
        # the subquery filters reservations with the same rental, OuterRef references the rental of current query object 
        #  filters previous reservations by previous checkin dates, OuterRef references the checkin date of current query object
        #  orders results by descending checkin
        #  slices the pk of the first result, which is the reservation with prior and closest date
        sub_query = Reservation.objects.filter(rental=OuterRef(    
            "rental"), checkin__lt=OuterRef("checkin")).order_by("-checkin").values("pk")[:1]
        return Reservation.objects.order_by('rental', 'checkin').annotate(previous_reservation_id=Subquery(sub_query))
