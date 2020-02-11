from lists.models import Item
from django.test import TestCase


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = Item()
        second_item.text = "The second item"
        second_item.save()

        saved_items = Item.objects.all()

        self.assertEqual(saved_items.count(), 2)

        first_item_saved = saved_items[0]
        second_item_saved = saved_items[1]

        self.assertEqual(first_item_saved.text, "The first (ever) list item")
        self.assertEqual(second_item_saved.text, "The second item")
