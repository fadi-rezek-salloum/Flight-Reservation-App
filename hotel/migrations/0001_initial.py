# Generated by Django 4.0 on 2022-08-13 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('going_to', models.CharField(max_length=50)),
                ('pool', models.BooleanField(default=False)),
                ('breakfast_included', models.BooleanField(default=False)),
                ('free_airport_shuttle', models.BooleanField(default=False)),
                ('business_services', models.BooleanField(default=False)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('number_of_people', models.PositiveIntegerField(default=1)),
                ('rating', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
                ('ac_tv', models.BooleanField()),
                ('image', models.ImageField(upload_to='rooms/')),
                ('image2', models.ImageField(upload_to='rooms/')),
                ('image3', models.ImageField(upload_to='rooms/')),
                ('image4', models.ImageField(upload_to='rooms/')),
                ('image5', models.ImageField(upload_to='rooms/')),
                ('price_per_24_h', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('if_free', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('number_of_days', models.PositiveIntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
    ]