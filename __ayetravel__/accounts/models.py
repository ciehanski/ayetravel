from django.db import models
from django.contrib.auth.models import User
from trips.models import Trips
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    mfa = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    location = models.CharField(max_length=264, blank=True)
    age = models.IntegerField(default=0)
    pins = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'userprofile'
        verbose_name_plural = 'userprofiles'

    def __str__(self):
        return f'User profile & settings for the user: {self.user_id.get_username()}'


class UserNotifications(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    # TODO build out notification system
    def create_notification(self, instance, message):
        new_notif = UserNotifications.objects.create(user_id=instance, message=message)
        return new_notif

    def read_notification(self):
        self.read = True

    def delete_notification(self, instance, message, timestamp):
        UserNotifications.objects.delete(user_id=instance, message=message, timestamp=timestamp)

    def __str__(self):
        return str('"' + self.message + '"' + ' for the user: ' + self.user_id.get_username())


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user_id=instance)


@receiver(post_save, sender=User)
def delete_userprofile(sender, instance, **kwargs):
    instance.userprofile.delete()


@receiver(post_save, sender=User)
def save_userprofile(sender, instance, **kwargs):
    instance.userprofile.save()
