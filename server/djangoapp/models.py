from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib import admin
# from django.utils.timezone import now
# from .models import CarMake, CarModel


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Other fields as needed
    def __str__(self):
        # Return the name as the string representation
        return self.name


class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2015)]
    )

    # Other fields as needed
    def __str__(self):
        # Return the name as the string representation
        return self.name


# Registering models with their respective admins
admin.site.register(CarMake)
admin.site.register(CarModel)
