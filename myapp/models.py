import datetime
import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

TELEFON_REGEX = RegexValidator(r'^[+]\d{3}( \d{3}){3}$', 'Wrong format')


# Create your models here.

class Client(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Enter your email',
                              error_messages={'unique': 'This email adress is already in use',
                                              'invalid': 'Invalid email adress',
                                              'blank': 'The field has to be filled'})
    phone = models.CharField(max_length=16, verbose_name='Phone number',
                             help_text='Enter your phone number like this: +420 123 123 123',
                             blank=True, validators=[TELEFON_REGEX])

    class Meta:
        ordering = ['client']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.client}'


class Piercer(models.Model):
    name = models.CharField(max_length=30, verbose_name='Piercer', help_text='Add a piercer')

    class Meta:
        verbose_name = 'Piercer'
        verbose_name_plural = 'Piercers'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Placement(models.Model):
    name = models.CharField(max_length=30, verbose_name='Placement')

    class Meta:
        verbose_name = 'Placement'
        verbose_name_plural = 'Placements'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Material(models.Model):
    name = models.CharField(max_length=30, verbose_name='Material')

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Thickness(models.Model):
    thickness = models.FloatField()

    class Meta:
        verbose_name = "Thickness"
        verbose_name_plural = "Thicknesses"
        ordering = ['thickness']

    def __str__(self):
        return f'{self.thickness}'


class Piercing(models.Model):
    placement = models.ForeignKey("Placement", on_delete=models.CASCADE)
    material = models.ForeignKey("Material", on_delete=models.CASCADE)
    thickness = models.ForeignKey("Thickness", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.placement}, {self.thickness} mm {self.material}'


class Salon(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.city}'


class Reservation(models.Model):
    customer = models.ForeignKey("Client", on_delete=models.CASCADE)
    piercer = models.ForeignKey("Piercer", on_delete=models.CASCADE)
    piercing = models.ForeignKey(Piercing, on_delete=models.CASCADE)
    date = models.DateTimeField()
    city = models.ForeignKey("Salon", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer}, {self.date}, {self.piercing}'

