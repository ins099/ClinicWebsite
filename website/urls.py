from django.urls import path
from .views import bookingAppointment,home,about,service,pricing,contact

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('service', service, name='service'),
    path('pricing', pricing, name='pricing'),
    path('contact', contact, name='contact'),
    path('appointment', bookingAppointment, name= 'appointment')
]