from django.test import TestCase
from django.urls import reverse, resolve


class TestUrls(TestCase):

    def test_detail_url(self):
        path = reverse('community:community_trips_detailed', kwargs={'slug': 'test-page'})
        assert resolve(path).view_name == 'community:community_trips_detailed'

    def test_list_url(self):
        path = reverse('community:community_trips_list')
        assert resolve(path).view_name == 'community:community_trips_list'
