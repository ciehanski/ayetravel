# Generated by Django 2.1.1 on 2018-09-18 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0015_pins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='trips/trip_files'),
        ),
    ]
