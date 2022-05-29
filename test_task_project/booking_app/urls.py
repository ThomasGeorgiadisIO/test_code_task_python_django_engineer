from django.conf import settings
from django.urls import path, include
from booking_app import views
import debug_toolbar



urlpatterns = [
    path('', views.ReservationList.as_view(), name='reservation_list'),
    path('__debug__/', include(debug_toolbar.urls)),
]


    
    