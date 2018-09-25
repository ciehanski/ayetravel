from django.test import TestCase, RequestFactory
from django.urls import reverse, resolve
from mixer.backend.django import mixer
import pytest
from accounts.models import InsensitiveUser
from trips.views import TripsDetailed


class TestUrls(TestCase):

    def test_detail_url(self):
        path = reverse('trips:trips_detailed', kwargs={'slug': 'test-page'})
        assert resolve(path).view_name == 'trips:trips_detailed'

    # def test_update_url(self):
    #     path = reverse('trips:trips_detailed', kwargs={'slug': 'test-page'})
    #     assert resolve(path).view_name == 'trips:trips_detailed'

    # def test_delete_url(self):
    #     path = reverse('trips:trips_detailed', kwargs={'slug': 'test-page'})
    #     assert resolve(path).view_name == 'trips:trips_detailed'

    def test_list_url(self):
        path = reverse('trips:trips_list')
        assert resolve(path).view_name == 'trips:trips_list'

    def test_create_url(self):
        path = reverse('trips:create_trip')
        assert resolve(path).view_name == 'trips:create_trip'


# class TestViews(TestCase):
#
#     def test_trips_detailed_view_auth(self):
#         path = reverse('trips:trips_detailed', kwargs={'slug': 'test'})
#         request = RequestFactory().get(path)
#         request.user = mixer.blend(InsensitiveUser)
#         trip = mixer.blend('trips.Trips', slug='test')
#         trip.user_id = request.user
#         response = TripsDetailed(request, slug='test')
#         assert response.status_code == 200
#
#
# @pytest.mark.django_db
# class TestModels(TestCase):
#
#     def test_trip_model_pins(self):
#         user = InsensitiveUser.objects.create()
#         trip_ = mixer.blend('trips.Trips', user_id=user)
#         mixer.blend('trips.Pins', trip=trip_)
#         assert trip_.get_pins == 1
#
#     def test_trip_model_comments(self):
#         trip_ = mixer.blend('trips.Trips')
#         mixer.blend('trips.Comments', trip=trip_)
#         assert trip_.get_comments == 1
#
#     def test_trip_model_participants(self):
#         trip_ = mixer.blend('trips.Trips')
#         mixer.blend('trips.Participants', trip=trip_)
#         assert trip_.get_comments == 1
