from django.db import models

class Rental(models.Model):
    name = models.CharField(max_length=20)

class Reservation(models.Model):
    rental_id = models.ForeignKey(to=Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
