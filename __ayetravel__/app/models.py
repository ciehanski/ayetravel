from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


class Trips(models.Model):
    owner = models.ForeignKey(User, on_delete='', default='')
    user_location = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(str(datetime.date.today()))
    end_date = models.DateField(str(datetime.date.today()))
    budget = models.IntegerField()
    participants = models.IntegerField()

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('app:trips_detailed', kwargs={'pk': self.pk})


class TravelLogs(models.Model):
    owner = models.ForeignKey(User, on_delete='', default='')
    user_location = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(str(datetime.date.today()))
    end_date = models.DateField(str(datetime.date.today()))
    budget = models.IntegerField()
    participants = models.IntegerField()

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse('app:travel_log_detailed', kwargs={'pk': self.pk})
