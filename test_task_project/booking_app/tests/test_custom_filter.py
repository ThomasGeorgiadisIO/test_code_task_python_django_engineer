from django.test import TestCase
from ..models import Rental, Reservation
from ..templatetags.custom_filter import ReservationFilter

class FilterTestCase(TestCase):
    '''Test class for the custom filter'''
    def setUp(self):
        self.rental1 = Rental.objects.create(name="rental1")
        self.reservation1 = Reservation.objects.create(rental=self.rental1, checkin="2022-05-05", checkout="2022-05-10")
        self.reservation2 = Reservation.objects.create(rental=self.rental1, checkin="2022-05-12", checkout="2022-05-15")
        self.reservation_list = [self.reservation1, self.reservation2]
    def test_custom_filter_without_previous_reservation(self):
        '''Test that the filter returns -- when there is no previous reservation'''
        self.assertEqual(ReservationFilter.previous_reservation_pk_filter(self.reservation_list)[0].previous_reservation_pk, "--")

    def test_custom_filter_with_previous_reservation(self):
        '''Test that the filter returns previous reservation'''
        self.assertEqual(ReservationFilter.previous_reservation_pk_filter(self.reservation_list)[1].previous_reservation_pk, self.reservation_list[0].pk)
        