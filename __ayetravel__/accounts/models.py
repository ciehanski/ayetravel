from django.db import models
from trips.models import Trips, Pins, Comments
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, UserManager, User


# User manager for insensitivity towards cases for username authentication
class InsensitiveUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


# User object for insensitivity towards cases for username authentication
class InsensitiveUser(AbstractUser):
    objects = InsensitiveUserManager()


class Profile(models.Model):
    user_id = models.OneToOneField(InsensitiveUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='profile_pictures/default.png')
    mfa = models.BooleanField(default=False)
    receive_emails = models.BooleanField(default=True)
    location = models.CharField(max_length=264, blank=True)
    age = models.IntegerField(default=0)
    pins = models.IntegerField(default=0)
    private_account = models.BooleanField(default=False)
    timezone = models.CharField(max_length=3, default='UTC')

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    @property
    def get_profile_picture(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return 'media/profile_pictures/default.png'

    def __str__(self):
        return f'User profile & settings for the user: {self.user_id.username}'


class UserNotifications(models.Model):
    user_id = models.ForeignKey(InsensitiveUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'notification'
        verbose_name_plural = 'notifications'

    def read_notification(self):
        self.read = True
        self.save()

    def delete_notification(self):
        self.delete()

    def __str__(self):
        return str('"' + self.message + '"' + ' for the user: ' + self.user_id.username)


def create_notification(user, message_):
    UserNotifications.objects.create(user_id=user, message=message_)


class UserCalendar(models.Model):
    user_id = models.OneToOneField(InsensitiveUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'usercalendar'
        verbose_name_plural = 'usercalendars'

    def __str__(self):
        return f'Calendar data for the user: {self.user_id.username}'


@receiver(post_save, sender=InsensitiveUser)
def save_or_create_user_objs(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user_id=instance)
        UserCalendar.objects.get_or_create(user_id=instance)
    instance.profile.save()
    instance.usercalendar.save()


@receiver(post_delete, sender=InsensitiveUser)
def delete_user_objs(sender, instance, **kwargs):
    instance.profile.delete()
    instance.usercalendar.delete()
    for trip in Trips.objects.all().filter(user_id__username__iexact=User.get_username(instance)):
        trip.delete()
    for comment in Comments.objects.all().filter(user_id__username__iexact=User.get_username(instance)):
        comment.delete()
    for pin in Pins.objects.all().filter(user_id__username__iexact=User.get_username(instance)):
        pin.delete()
    for notif in UserNotifications.objects.all().filter(user_id__username__iexact=User.get_username(instance)):
        notif.delete()
