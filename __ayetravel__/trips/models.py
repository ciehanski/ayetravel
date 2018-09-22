from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from ayetravel.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
import datetime


class Trips(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, default='', blank=True)
    name = models.CharField(max_length=50, default='')
    user_location = models.CharField(max_length=100, default='')
    destination = models.CharField(max_length=100, default='')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    budget = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='trips/trip_pictures', blank=True, null=True)
    public = models.BooleanField(default=False)
    packing_list = models.TextField(max_length=2000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    files = models.FileField(upload_to='trips/trip_files', null=True, blank=True)
    comments_obj = models.ForeignKey('Comments', on_delete=models.CASCADE, default=None)
    comments_total = models.IntegerField(default=0)
    pins_obj = models.ForeignKey('Pins', on_delete=models.CASCADE, default=None)
    pins_total = models.IntegerField(default=0)
    participants_obj = models.ForeignKey('Participants', on_delete=models.CASCADE, default=None)
    participants_total = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'trip'
        verbose_name_plural = 'trips'
        # TODO research trip permissions
        # permissions = (
        #     ("view_trip", "Can view this specific trip."),
        #     ("modify_trip", "Can modify this specific trip."),
        #     ("delete_trip", "Can remove this specific trip."))

    # TODO create comment form
    # def add_comment(self, request, trip_pk):
    #     trip = get_object_or_404(Trips, pk=trip_pk)
    #     if request.method == 'POST':
    #         form = CommentForm(request.POST)
    #         if form.is_valid():
    #             comment = form.save(commit=False)
    #             comment.trip = trip
    #             comment.save()
    #             self.comments_total += 1
    #             return redirect('trips:trips_detailed', slug=trip.slug)
    #     else:
    #         form = CommentForm()
    #     return render(request, 'trips/trips_detailed.html', {'form': form})

    def add_pin(self, user):
        # create pin and add it to my list of pin objects in trip, add tally to pin total
        self.pins_obj += Pins.objects.create(user_id=user, trip=self)
        self.pins_total += 1
        self.save()

    def add_participant(self, user):
        # create participant and add it to my list of participant objects in trip, add tally to participant total
        self.participants_obj += Participants.objects.create(user_id=user, trip=self)
        self.participants_total += 1
        self.save()

    def get_participants(self):
        all_participants = []
        for participants in Participants.objects.all().filter(trip_id__exact=self.id):
            all_participants += participants
        return all_participants

    def get_comments(self):
        all_com = []
        for comment in Comments.objects.all().filter(trip_id__exact=self.id):
            all_com += comment
        return all_com

    def get_status(self):
        if self.start_date <= datetime.date.today() and not self.end_date >= datetime.date.today():
            return 'in_progress'
        elif self.start_date > datetime.date.today():
            return 'coming_up'
        elif self.end_date < datetime.date.today():
            return 'completed'

    def __str__(self):
        return str(f'Trip ID: ' + str(self.pk) + ' "' + self.name + '"' + ' created by '
                   + str(self.user_id.username))

    def get_absolute_url(self):
        return reverse('trips:trips_detailed', kwargs={'slug': self.slug})


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
                   + str(self.user_id.username) + ' left on Trip ID: ' + self.trip.pk)

    def get_absolute_url(self):
        return reverse('trips:trips_detailed', kwargs={'slug': self.trip.slug})


class Pins(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'pin'
        verbose_name_plural = 'pins'

    def __str__(self):
        return str(f'Pin ID: ' + str(self.pk) + ' for trip: '
                   + '"' + self.trip.name + '"' + 'left by user: ' + self.user_id.username)

    def get_absolute_url(self):
        return reverse('trips:trips_detailed', kwargs={'slug': self.trip.slug})


class Participants(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'participant'
        verbose_name_plural = 'participants_total'

    def __str__(self):
        return str(f'Participant: ' + self.user_id.username + " for trip: " + self.trip.pk)

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'username': self.user_id.username})


class DailyLog(models.Model):
    trip = models.OneToOneField(Trips, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'dailylog'


class Excursions(models.Model):
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'excursion'
        verbose_name_plural = 'excursions'


class Itinerary(models.Model):
    trip = models.OneToOneField(Trips, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'itinerary'


@receiver(post_save, sender=Trips)
def save_or_create_user_objs(sender, instance, created, **kwargs):
    if created:
        Itinerary.objects.get_or_create(user_id=instance)
        DailyLog.objects.get_or_create(user_id=instance)
    instance.itinerary.save()
    instance.dailylog.save()


@receiver(pre_save, sender=Trips)
def gen_slug(sender, instance, *args, **kwargs):
    if instance.slug == '':
        instance.slug = unique_slug_generator(instance)
