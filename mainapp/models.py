from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    volume = models.FloatField()
    fuel_type = models.CharField(max_length=50)
    transmission_type = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/')
    is_free = models.BooleanField(default=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'


class User(models.Model):
    name = models.CharField(max_length=255)
    agent = models.CharField(max_length=255)
    date_out = models.DateField()
    time_out = models.TimeField()
    date_in = models.DateField()
    time_in = models.TimeField()
    fuel = models.CharField(max_length=16)
    milage = models.IntegerField()
    notes = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='car')

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

