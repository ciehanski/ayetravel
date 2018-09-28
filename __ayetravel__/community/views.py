from trips.views import TripsDetailed, TripsList


class CommunityTripsList(TripsList):
    context_object_name = 'community_trips_list'
    template_name = 'community/community_list.html'


class CommunityTripsDetailed(TripsDetailed):
    context_object_name = 'community_trips_detailed'
    template_name = 'community/community_detailed.html'
