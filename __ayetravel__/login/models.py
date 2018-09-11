from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    mfa = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    location = models.CharField(max_length=264, blank=True)
    age = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'usersettings'
        verbose_name_plural = 'usersettings'

    def __str__(self):
        return f'User settings for {self.user.get_username}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserSettings.objects.create(user=instance)
        UserNotifications.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # instance.profile.save()
    instance.usersettings.save()
    instance.usernotifications.save()


class UserNotifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    message = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now(), editable=False)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('login:index', kwargs={'pk': self.pk})
