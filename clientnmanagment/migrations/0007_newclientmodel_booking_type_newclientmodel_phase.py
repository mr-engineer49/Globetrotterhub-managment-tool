# Generated by Django 5.0.3 on 2024-03-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientnmanagment', '0006_remove_newclientmodel_booking_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newclientmodel',
            name='booking_type',
            field=models.CharField(blank=True, default=[('H', 'Hotel'), ('V', 'Vacations'), ('P', 'Places')], max_length=50),
        ),
        migrations.AddField(
            model_name='newclientmodel',
            name='phase',
            field=models.CharField(blank=True, default=[('C', 'Created'), ('R', 'Running / Active'), ('F', 'Finished')], max_length=50),
        ),
    ]
