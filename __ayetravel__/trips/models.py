from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ayetravel.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Trips(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, default='', blank=True)
    name = models.CharField(max_length=50, blank=True)
    user_location = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    budget = models.IntegerField(default=0)
    participants_total = models.IntegerField(default=1)
    comments_total = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='trips/trip_pictures', blank=True, null=True)
    public = models.BooleanField(default=False)
    pins_total = models.IntegerField(default=0)
    packing_list = models.TextField(blank=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    files = models.FilePathField(path='trips/trip_files', null=True, blank=True)

    class Meta:
        verbose_name = 'trip'
        verbose_name_plural = 'trips'
        # TODO research trip permissions
        # permissions = (
        #     ("view_trip", "Can view this specific trip."),
        #     ("modify_trip", "Can modify this specific trip."),
        #     ("delete_trip", "Can remove this specific trip."))

    def __str__(self):
        return str(f'Trip ID: ' + str(self.pk) + ' "' + self.name + '"' + ' created by '
                   + str(self.user_id.get_username()))

    def get_absolute_url(self):
        return reverse('app:trips_detailed', kwargs={'slug': self.slug})


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return str(f'Comment ID: ' + str(self.pk) + ' "' + self.message + '"' + ' created by '
                   + str(self.user_id.get_username()) + ' left on Trip ID: ' + self.trip.pk)


class Participants(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'participant'
        verbose_name_plural = 'participants_total'

    # def __str__(self):
    #     return str(f'Comment ID: ' + str(self.pk) + ' "' + self.message + '"' + ' created by '
    #                + str(self.user_id.get_username()) + ' left on Trip ID: ' + self.trip.pk)


def pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Trips)
