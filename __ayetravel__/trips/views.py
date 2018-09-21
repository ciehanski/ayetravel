from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from trips.forms import CreateTripForm
from trips.models import Trips
from app.views import BaseViewMixin


class TripsDetailed(BaseViewMixin, DetailView):
    context_object_name = 'trips_detailed'
    template_name = 'trips/trips_detailed.html'
    object = Trips

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trips'] = self.cleaned_object(request)
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)

    def cleaned_object(self, request):
        slug_ = self.kwargs.get('slug')
        obj = self.get_object()
        if obj.user_id.get_username() == request.user.get_username() or obj.public:
            return get_object_or_404(Trips, slug=slug_)
        else:
            return render(request, 'app/base.html', {'error': 'This is a private trip which you '
                                                              'do not have permissions to view.'})


class CreateTrip(BaseViewMixin, CreateView):
    context_object_name = 'create_trip'
    template_name = 'trips/create_trip.html'
    form_class = CreateTripForm
    success_url = reverse_lazy('trips:trips_detailed')

    def form_valid(self, form):
        new_trip = form.save(commit=False)
        new_trip.save()

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

    def post(self, request, *args, **kwargs):
        pass


class TripsList(BaseViewMixin, ListView):
    context_object_name = 'trips_list'
    template_name = 'trips/trips_list.html'
    object_list = Trips.objects.all()
