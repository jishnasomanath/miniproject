# Generated by Django 3.2.5 on 2021-12-13 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_SS_App', '0012_merchant_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='pesticide_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmername', models.CharField(max_length=100)),
                ('pesticidename', models.CharField(max_length=100)),
                ('pesticideprice', models.CharField(max_length=100)),
            ],
        ),
    ]
