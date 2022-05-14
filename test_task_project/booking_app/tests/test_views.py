from django.test import TestCase, Client
from django.urls import reverse
from ..models import Rental, Reservation

class TestReservationListView(TestCase):
    '''Test class for reservation list view functionality'''
    def setUp(self):
        self.client = Client()
        self.rental1 = Rental.objects.create(name="rental1")
        self.rental2 = Rental.objects.create(name="rental2")
        self.reservation1 = Reservation.objects.create(rental_id=self.rental1, checkin="2022-05-05", checkout="2022-05-10")
        self.reservation2 = Reservation.objects.create(rental_id=self.rental1, checkin="2022-05-12", checkout="2022-05-15")
        self.reservation3 = Reservation.objects.create(rental_id=self.rental2, checkin="2022-05-05", checkout="2022-05-10")
        self.reservation4 = Reservation.objects.create(rental_id=self.rental2, checkin="2022-05-12", checkout="2022-05-15")

    def test_view_url_exists_at_desired_location(self):
        '''Test that the url exists'''
        response = self.client.get(reverse('reservation_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        '''Test that the correct template is rendered'''
        response = self.client.get(reverse('reservation_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking_app/reservation_list.html')

    def test_view_uses_all_data(self):
        '''Test that context has all the objects from DB'''
        response = self.client.get(reverse('reservation_list'))
        self.assertEqual(len(response.context['object_list']), 4)

    def test_view_uses_correct_rental_order(self):
        '''Test the order by rental'''
        response = self.client.get(reverse('reservation_list'))
        reservation_with_rental1_list = response.context['object_list'][:2]
        reservation_with_rental2_list = response.context['object_list'][2:]
        self.assertTrue(all(e.rental_id==self.rental1 for e in reservation_with_rental1_list))
        self.assertTrue(all(e.rental_id==self.rental2 for e in reservation_with_rental2_list))

    def test_view_uses_correct_reservation_order(self):
        '''Test the order by check in date'''
        response = self.client.get(reverse('reservation_list'))
        reservation_with_rental1_list = response.context['object_list'][:2]
        reservation_with_rental2_list = response.context['object_list'][2:]
        self.assertTrue(reservation_with_rental1_list[0].checkin < reservation_with_rental1_list[1].checkin)
        self.assertTrue(reservation_with_rental2_list[0].checkin < reservation_with_rental2_list[1].checkin)
