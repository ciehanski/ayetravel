# Generated by Django 2.1.1 on 2018-09-15 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(default='page-title', max_length=150, unique=True)),
                ('user_location', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('destination', models.CharField(blank=True, max_length=100)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('budget', models.IntegerField(default=0)),
                ('participants_total', models.IntegerField(default=0)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='trip_pictures')),
                ('public', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('pins', models.IntegerField(default=0)),
                ('packing_list', models.TextField(blank=True, max_length=2000)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'trip',
                'verbose_name_plural': 'trips',
            },
        ),
    ]
