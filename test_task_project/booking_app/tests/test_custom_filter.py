from django.test import TestCase
from ..models import Rental, Reservation
from ..templatetags.custom_filter import ReservationFilter

class FilterTestCase(TestCase):
    '''Test class for the custom filter'''
    def setUp(self):
        self.rental1 = Rental.objects.create(name="rental1")
        self.reservation1 = Reservation.objects.create(rental_id=self.rental1, checkin="2022-05-05", checkout="2022-05-10")
        self.reservation2 = Reservation.objects.create(rental_id=self.rental1, checkin="2022-05-12", checkout="2022-05-15")

    def test_custom_filter_without_previous_reservation(self):
        '''Test that the filter returns -- when there is no previous reservation'''
        self.assertEqual(ReservationFilter.previous_res_id(self.reservation1), "--")

    def test_custom_filter_with_previous_reservation(self):
        '''Test that the filter returns previouw reservation'''
        self.assertEqual(ReservationFilter.previous_res_id(self.reservation2), self.reservation1.pk)
        