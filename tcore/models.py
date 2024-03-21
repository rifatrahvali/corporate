from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()