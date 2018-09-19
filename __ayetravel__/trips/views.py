from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from trips.forms import CreateTripForm
from trips.models import Trips
from app.views import render_user_trips, render_community_trips, render_user_notifications


class TripsDetailed(LoginRequiredMixin, DetailView):
    context_object_name = 'trips_detailed'
    template_name = 'trips/trips_detailed.html'
    object = Trips

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['community_trips'] = render_community_trips(request)
        context['trips'] = self.clean_object(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)

    def clean_object(self, request):
        slug_ = self.kwargs.get('slug')
        obj = self.get_object()
        if obj.user_id.get_username() == request.user.get_username() or obj.public:
            return get_object_or_404(Trips, slug=slug_)
        else:
            return render(request, 'app/500.html', {'error': 'This is a private trip which you '
                                                             'do not have permissions to view.'})


class CreateTrip(LoginRequiredMixin, CreateView):
    context_object_name = 'create_trip'
    template_name = 'trips/create_trip.html'
    form_class = CreateTripForm
    object = Trips

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notifs'] = render_user_notifications(request)
        context['notifs_total'] = len(render_user_notifications(request))
        context['name'] = self.form_class.name
        context['user_location'] = self.form_class.user_location
        context['destination'] = self.form_class.destination
        context['budget'] = self.form_class.budget
        context['packing_list'] = self.form_class.packing_list
        context['participants_total'] = self.form_class.participants_total
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateTrip(LoginRequiredMixin, UpdateView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    # form_class = UpdateTripForm

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trips'] = self.get_object()
        context['notifs'] = render_user_notifications(request)
        context['notifs_total'] = len(render_user_notifications(request))
        return render(request, self.template_name, context)

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DeleteTrip(LoginRequiredMixin, DeleteView):
    context_object_name = 'update_trip'
    template_name = 'trips/create_trip.html'
    model = Trips
    success_url = reverse_lazy('app:trips_list')

    def get_object(self, queryset=Trips):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Trips, slug=slug_)

    def post(self, request, *args, **kwargs):
        pass


class TripsList(LoginRequiredMixin, ListView):
    context_object_name = 'trips_list'
    template_name = 'trips/trips_list.html'
    object_list = Trips.objects.all()

    def get(self, request, *args, **kwargs):
        self.object_list = render_user_trips(request)
        context = super().get_context_data(**kwargs)
        context['trips'] = render_user_trips(request)
        context['notifs'] = render_user_notifications(request)
        context['trips_total'] = len(render_user_trips(request))
        context['notifs_total'] = len(render_user_notifications(request))
        return render(request, self.template_name, context)
