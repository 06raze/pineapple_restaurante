from django.views.generic import DetailView, ListView

from .models import *


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class ReservaListView(ListView):
    model = Reserva

class ReservaDetailView(DetailView):
    model = Reserva
