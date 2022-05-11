from django.urls import path
from booking_app import views

urlpatterns = [
    path('', views.ReservationList.as_view()),
]