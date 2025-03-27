from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Car(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('sold', 'Sold'),
    ]

    name = models.CharField(max_length=100)
    year = models.IntegerField()
    body_type = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    mileage = models.PositiveIntegerField()
    seats = models.IntegerField()
    engine_type = models.CharField(max_length=50)
    mpg = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.name} - {self.status}"


class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
        ('lost', 'Lost'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    zip_code = models.CharField(max_length=10)
    message = models.TextField(blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='leads')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead for {self.car.name} by {self.name} - {self.status}"
