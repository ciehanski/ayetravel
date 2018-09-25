from django.test import TestCase
from django.urls import resolve, reverse


class TestUrls(TestCase):

    def test_index_url(self):
        path = reverse('app:index')
        assert resolve(path).view_name == 'app:index'

    def test_search_url(self):
        path = reverse('app:search')
        assert resolve(path).view_name == 'app:search'
