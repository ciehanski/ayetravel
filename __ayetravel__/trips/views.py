from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from trips.forms import CreateTripForm
from trips.models import Trips
from app.views import IndexView


class TripsDetailed(IndexView, DetailView):
    context_object_name = 'trips_detailed'
    template_name = 'trips/trips_detailed.html'
    queryset = Trips.objects.all()
    object = Trips

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trips'] = self.clean_object(request)
        return render(request, self.template_name, context)

    def clean_object(self, request):
        slug_ = self.kwargs.get('slug')
        obj = self.get_object()
        if obj.user_id.get_username() == request.user.get_username() or obj.public:
            return get_object_or_404(Trips, slug=slug_)
        else:
            return render(request, 'app/500.html', {'error': 'This is a private trip which you '
                                                             'do not have permissions to view.'})


class CreateTrip(IndexView, CreateView):
    context_object_name = 'create_trip'
    template_name = 'trips/create_trip.html'
    form_class = CreateTripForm
    object = Trips

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTrip(IndexView, UpdateView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    # form_class = UpdateTripForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteTrip(IndexView, DeleteView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    model = Trips
    success_url = reverse_lazy('app:trips_list')

    def post(self, request, *args, **kwargs):
        pass


class TripsList(IndexView, ListView):
    context_object_name = 'trips_list'
    template_name = 'trips/trips_list.html'
    object_list = Trips.objects.all()
