# Generated by Django 3.2.5 on 2021-12-13 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_SS_App', '0014_pesticide_order_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pesticide_order_table',
        ),
    ]