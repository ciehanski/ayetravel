# Generated by Django 2.1.1 on 2018-09-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travellogs', '0002_auto_20180915_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travellogs',
            name='slug',
            field=models.SlugField(default='page-slug', max_length=150, unique=True),
        ),
    ]
