from django.contrib import admin
from .models import Piercer, Client, Material, Thickness, Placement, Piercing, Salon, Reservation

# Register your models here.

admin.site.register(Piercer)
admin.site.register(Client)
admin.site.register(Material)
admin.site.register(Thickness)
admin.site.register(Placement)
admin.site.register(Piercing)
admin.site.register(Salon)
admin.site.register(Reservation)