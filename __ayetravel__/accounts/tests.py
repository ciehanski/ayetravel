from django.test import TestCase
from django.urls import resolve, reverse


class TestUrls(TestCase):

    def test_index_url(self):
        path = reverse('accounts:index')
        assert resolve(path).view_name == 'accounts:index'

    def test_login_url(self):
        path = reverse('accounts:login')
        assert resolve(path).view_name == 'accounts:login'

    def test_logout_url(self):
        path = reverse('accounts:logout')
        assert resolve(path).view_name == 'accounts:logout'

    # def test_recovery_url(self):
    #     path = reverse('accounts:recovery')
    #     assert resolve(path).view_name == 'accounts:recovery'

    def test_profile_url(self):
        path = reverse('accounts:profile', kwargs={'username': 'ciehanski'})
        assert resolve(path).view_name == 'accounts:profile'
