from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class UserSettings(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    mfa = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    location = models.CharField(max_length=264, blank=True)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'usersettings'
        verbose_name_plural = 'usersettings'

    def __str__(self):
        return f'User settings for {str(self.user_id.get_username())}'


class UserNotifications(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    message = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def __str__(self):
        return str('"' + self.message + '"' + ' for the user: ' + self.user_id.get_username())

    def get_absolute_url(self):
        return reverse('login:index', kwargs={'pk': self.pk})
