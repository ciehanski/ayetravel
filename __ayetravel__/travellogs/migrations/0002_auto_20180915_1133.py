# Generated by Django 2.1.1 on 2018-09-15 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travellogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travellogs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
