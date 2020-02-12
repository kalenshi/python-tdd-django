from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')

        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>To-Do list</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_post(self):
        self.client.post('/', data={'item_text': "A new list item"})
        self.assertEqual(Item.objects.count(), 1)

    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': "A new list item"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')


    def test_displays_all_list_items(self):
        Item.objects.create(text="itemey 1")
        Item.objects.create(text="itemey 2")

        response = self.client.get('/')
        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())


