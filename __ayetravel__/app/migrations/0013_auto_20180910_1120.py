# Generated by Django 2.1.1 on 2018-09-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180910_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='travellogs',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='trips',
            name='picture',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
