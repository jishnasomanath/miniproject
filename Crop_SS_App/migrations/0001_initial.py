# Generated by Django 3.2.5 on 2021-11-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_signup_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmername', models.CharField(max_length=100)),
                ('farmerplace', models.CharField(max_length=100)),
                ('farmerphone', models.CharField(max_length=15)),
                ('fusername', models.CharField(max_length=100)),
                ('fpassword', models.CharField(max_length=100)),
                ('fconfirmpassword', models.CharField(max_length=100)),
            ],
        ),
    ]