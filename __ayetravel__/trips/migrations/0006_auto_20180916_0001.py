# Generated by Django 2.1.1 on 2018-09-16 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20180915_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='participants',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='trips',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=100, unique=True),
        ),
    ]
