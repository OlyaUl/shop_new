from django.db import models
from datetime import datetime


class CarModel(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return '{0}'.format(self.title)


class Color(models.Model):
    title = models.CharField(max_length=30)
    code_color = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.title


class Specifications(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    scope = models.IntegerField()
    power = models.IntegerField()
    FULL = '1'
    FRONT = '2'
    REAR = '3'
    CARDAN = '4'
    BELT = '5'
    CHAIN = '6'
    DRIVE_TYPE = (
        (FULL, 'Full'),
        (FRONT, 'Front'),
        (REAR, 'Rear'),
        (CARDAN, 'Cardan'),
        (BELT, 'Belt'),
        (CHAIN, 'Chain'),
    )
    drive_type = models.CharField(max_length=2,
                                  choices=DRIVE_TYPE,
                                  default=FULL)
    PETROL = 'P'
    DIESEL = 'D'
    GAS = 'G'
    GAS_PETROL = 'GP'
    OTHER = 'O'
    FUEL = (
        (PETROL, 'Petrol'),
        (DIESEL, 'Diesel'),
        (GAS, 'Gas'),
        (GAS_PETROL, 'Gas/Petrol'),
        (OTHER, 'Senior'),
    )
    petrol = models.CharField(max_length=2,
                              choices=FUEL,
                              default=PETROL)


class Image(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(upload_to='all_img', blank=True)
    main_image = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=30)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    specifications = models.ForeignKey(Specifications, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, blank=True)
    year = models.IntegerField()

    def __str__(self):
        return '{0 1 2 }'.format(self.title, self.specifications, self.image)
