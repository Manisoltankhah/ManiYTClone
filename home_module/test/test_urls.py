from django.test import TestCase
from django.urls import reverse, resolve

import home_module.views
from home_module.views import IndexPageView

class TestUrls(TestCase):

    def test_index_page_url_is_resolved(self):
        url = reverse('home_page')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, IndexPageView)