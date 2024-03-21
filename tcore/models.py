from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()


class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

class Services(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.SlugField(max_length=200,blank=True, editable=False)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Services,self).save(*args, **kwargs)

# anasayfa'da bulunan slider 
class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider')