from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=150)
    content = RichTextField()


class Contact(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="isim soyisim")
    phone = models.CharField(max_length=15, verbose_name="telefon")
    email = models.EmailField(verbose_name="e-posta")
    message = models.TextField(verbose_name="mesaj")

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

#category
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,blank=True,editable=False)
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
            return self.title

#blog
class Blog(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blogs')
    content = RichTextField()
    publishDate = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=150)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200,unique=True,blank=True,editable=False)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog,self).save(*args, **kwargs)

    def __str__(self):
            return self.title
        
#site içerisinde ayarlar
class Settings(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    phone_fixed = models.CharField(max_length=15)
    phone_mobile = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=150)
    address = models.TextField()
    postal_code = models.CharField(max_length=15)
    facebook_url = models.URLField(max_length=255)
    x_url = models.URLField(max_length=255)
    instagram_url = models.URLField(max_length=255)
    youtube_url = models.URLField(max_length=255)
    logo_1 = models.ImageField(upload_to='dimg',null=True,blank=True)
    logo_2 = models.ImageField(upload_to='dimg',null=True,blank=True)