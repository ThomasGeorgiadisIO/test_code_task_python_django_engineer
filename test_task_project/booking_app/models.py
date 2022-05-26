from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=20)

# A many to one relationship with Rental
# Deleting a Rental will delete all Reservations related


class Reservation(models.Model):
    rental = models.ForeignKey(to=Rental, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
