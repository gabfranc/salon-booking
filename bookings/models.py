from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):  # Very important for display in the admin, etc.
        return self.name

class Booking(models.Model):  # And the Booking model (if you have it)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.service} - {self.date} {self.time}"