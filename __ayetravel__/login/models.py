from django.db import models
from django.contrib.auth.models import User


class UserSettings(models.Model):
    owner = models.ForeignKey(User, on_delete='', default='')
    profile_picture = models.ImageField()
    mfa = models.BooleanField()
    receive_emails = models.BooleanField()
    location = models.CharField(max_length=264)
    age = models.IntegerField()

    def __str__(self):
        return f'User settings for {self.owner.get_username}'


class UserNotifications(models.Model):
    owner = models.ForeignKey(User, on_delete='', default='')
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message
