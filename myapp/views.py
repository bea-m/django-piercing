from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from myapp.models import Reservation, Client
from django import forms

# Create your views here.


def index(request):
    return render(request, "index.html")


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['piercing', 'piercer', 'date', 'city']


def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            user = Client.objects.get(client_id=request.user.id)
            reservation.customer = user
            reservation.save()
            return redirect('reservations')

    else:
        form = ReservationForm()

    return render(request, 'reservations/create.html', {'form': form})


class ReservationList(ListView):
    model = Reservation
    template_name = "reservations/list.html"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = super(ReservationList, self).get_queryset()
            queryset = queryset.filter(customer__client=self.request.user)
            return queryset


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"



