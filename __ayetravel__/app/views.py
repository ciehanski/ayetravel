from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from trips.models import Trips


class BaseViewMixin(LoginRequiredMixin, object):
    context_object_name = 'base'
    template_name = 'app/base.html'

    def get(self, request, *args, **kwargs):
        # Search handling
        context = super().get_context_data(**kwargs)
        search_term = request.GET.get('search')
        if search_term is not None:
            search = Trips.objects.filter(name__icontains=search_term)
            if len(search) > 0:
                trips = []
                for trip in search:
                    trips.append(trip)
                context['search_results'] = trips
                return render(request, 'app/search.html', context)
            else:
                context['error'] = 'Nothing matched your search.'
                return render(request, 'app/search.html', context)
        else:
            # if search was blank, just re-render index page
            return render(request, self.template_name, context)


class IndexView(BaseViewMixin, TemplateView):
    context_object_name = 'index'
    template_name = 'app/index.html'


class SearchView(BaseViewMixin, ListView):
    context_object_name = 'search'
    template_name = 'app/search.html'
    object_list = Trips.objects.all()


class CalendarView(BaseViewMixin, TemplateView):
    context_object_name = 'calendar'
    template_name = 'app/calendar.html'


def handler404(request):
    return render(request, 'app/404.html', status=404)


def handler500(request):
    return render(request, 'app/500.html', status=500)
