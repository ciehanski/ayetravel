# Generated by Django 2.1.1 on 2018-09-18 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0013_remove_trips_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trips',
            old_name='pins',
            new_name='pins_total',
        ),
    ]