from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


class Trips(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    user_location = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(str(datetime.date.today()))
    end_date = models.DateField(str(datetime.date.today()))
    budget = models.IntegerField()
    participants = models.IntegerField()
    picture = models.ImageField(upload_to='trip_pictures/', null=True, blank=True)
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'trip'
        verbose_name_plural = 'trips'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('app:trips_detailed', kwargs={'pk': self.pk})


class TravelLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    user_location = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(str(datetime.date.today()))
    end_date = models.DateField(str(datetime.date.today()))
    budget = models.IntegerField(default=0)
    participants = models.IntegerField(default=1)
    picture = models.ImageField(upload_to='travellog_pictures/', null=True, blank=True)

    class Meta:
        verbose_name = 'travel_log'
        verbose_name_plural = 'travel_logs'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('app:travel_log_detailed', kwargs={'pk': self.pk})
