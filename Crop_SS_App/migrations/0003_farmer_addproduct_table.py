# Generated by Django 3.2.5 on 2021-12-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_SS_App', '0002_customer_signup_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_addproduct_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmername', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('Productcategory', models.CharField(max_length=100)),
                ('productprice_qty', models.CharField(max_length=100)),
            ],
        ),
    ]