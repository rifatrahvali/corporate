# Generated by Django 5.0.2 on 2024-03-21 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0006_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=150, verbose_name='isim soyisim'),
        ),
    ]
