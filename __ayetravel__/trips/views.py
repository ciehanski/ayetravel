from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from trips.forms import CreateTripForm, CommentForm
from trips.models import Trips
from app.views import BaseViewMixin


class TripsDetailed(BaseViewMixin, DetailView):
    context_object_name = 'trips_detailed'
    template_name = 'trips/trips_detailed.html'
    object = Trips

    # def get(self, request, *args, **kwargs):
    #     return render(request, 'trips/trips_detailed.html', {'comment_form': CommentForm()})

    def post(self, request, *args, **kwargs):
        form = CommentForm()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.trip = request.trip
            comment.save()
            comment.trip.comments_total += 1
            comment.trip.save()
            return redirect('trips:trips_detailed', slug=request.trip.slug)
        else:
            return render(request, 'trips/trips_detailed.html', {'comment_form': form})

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)


class CreateTrip(BaseViewMixin, CreateView):
    context_object_name = 'create_trip'
    template_name = 'trips/create_trip.html'
    form_class = CreateTripForm
    object = Trips
    success_url = reverse_lazy('trips:trips_detailed')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        pass


class UpdateTrip(BaseViewMixin, UpdateView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    # form_class = UpdateTripForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteTrip(BaseViewMixin, DeleteView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    object = Trips
    success_url = reverse_lazy('app:trips_list')


class TripsList(BaseViewMixin, ListView):
    context_object_name = 'trips_list'
    template_name = 'trips/trips_list.html'
    object_list = Trips.objects.all()
