from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


class Trips(models.Model):
    owner = models.ForeignKey(User, on_delete='', default='')
    user_location = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    date = models.DateField(str(datetime.datetime.now()))
    budget = models.IntegerField()
    participants = models.IntegerField()

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('app:trips_detailed', kwargs={'pk': self.pk})
