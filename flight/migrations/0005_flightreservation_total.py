# Generated by Django 4.0 on 2022-08-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='flightreservation',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]