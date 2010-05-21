#encoding: utf-8

from django.test import TestCase


class TestViews(TestCase):
    def test_show_lncc_event_page(self):
        response = self.client.get('/evento/istcc-p/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'event/lncc.html')

    def test_show_estacio_event_page(self):
        response = self.client.get('/evento/estacio/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'event/estacio.html')