# Generated by Django 2.1.1 on 2018-09-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0009_remove_trips_participants_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='trips',
            name='participants_total',
            field=models.IntegerField(default=1),
        ),
    ]
