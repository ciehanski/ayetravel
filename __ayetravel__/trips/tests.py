from django.test import TestCase
from django.urls import reverse, resolve


# TODO Write Trips tests
# class TestUrls(TestCase):
#
#     def test_detail_url(self):
#         response = self.client.get(reverse('trips_detailed', kwargs={'slug': 'test-page'}))
#         self.assertEqual(response.status_code, 200)
#
#     def test_update_url(self):
#         url = self.client.get(reverse('trips:update_trip'))
#         self.assertEqual(url, 'my/trips/update/test-page')
#
#     def test_delete_url(self):
#         url = reverse('delete_trip', kwargs={'slug': 'test-page'})
#         self.assertEqual(url, 'my/trips/delete/test-page')
#
#     def test_list_url(self):
#         url = reverse('trips_list')
#         self.assertEqual(url, 'my/trips/')
#
#     def test_create_url(self):
#         url = reverse('create_trip')
#         self.assertEqual(url, 'my/trips/create/')
#
#
# class TestViews(TestCase):
#
#     def test_update_view(self):
#         resolver = resolve('my/trips/update/')
#         self.assertEqual(resolver.view_name, 'update_trip')
#
#
# class TestModels(TestCase):
#
#     def test_trip_model(self):
#         pass
