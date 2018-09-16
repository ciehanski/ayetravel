from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ayetravel.utils import unique_slug_generator
from django.db.models.signals import pre_save


class TravelLogs(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, unique=True, default='page-slug')
    name = models.CharField(max_length=50, blank=True)
    user_location = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    budget = models.IntegerField(default=0)
    participants = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='trips/travellog_pictures', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'travel_log'
        verbose_name_plural = 'travel_logs'

    def __str__(self):
        return str('Travel Log ID: ' + self.pk + ' created by user ' + str(self.user_id.get_username()))

    def get_absolute_url(self):
        return reverse('app:travel_log_detailed', kwargs={'slug': self.slug})


def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_post_reciever, sender=TravelLogs)
