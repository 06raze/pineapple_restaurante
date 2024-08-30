from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name = 'base'),
    path('reserva/', ReservaListView.as_view(), name = 'reserva'),
    path('<slug:slug>/', ReservaDetailView.as_view(), name = 'dreserva'),

]