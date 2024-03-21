from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()