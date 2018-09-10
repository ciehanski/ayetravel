from django.db import models


class Trips(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=50)


class Notifications(models.Model):
    text = models.CharField(max_length=200)


class UserSettings(models.Model):
    profile_picture = models.ImageField()
