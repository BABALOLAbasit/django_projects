from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)  # Use CharField for phone numbers
    password = models.CharField(max_length=50)
    age = models.IntegerField()  # Removed max_length


    def __str__(self):
    	return self.first_name + ' ' + self.last_name + ' ' + self.email

