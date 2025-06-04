from django.db import models

class Delivery(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Use CharField for hashed passwords
    phone = models.CharField(max_length=15)  # Store phone numbers as strings

    def __str__(self):
        return self.name
