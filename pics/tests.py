from django.test import TestCase

from .models import *


# Create your tests here.
# Location category
class TestCategory(TestCase):
    def setUp(self):
        self.new_category = Category(name='cars')

    def test_category_instance(self):
        pass

    def test_save_category(self):
        before = Category.objects.count()
        self.new_category.save_category()
        after = Category.objects.count()
        self.assertTrue(before < after)

    def test_delete_category(self):
        before = Category.objects.count()
        self.new_category.delete_category()
        after = Category.objects.count()
        self.assertTrue(before > after)

    def tearDown(self):
        pass


# Location tests
class Location(TestCase):
    def setUp(self):
        pass

    def test_category_instance(self):
        pass

    def tearDown(self):
        pass


# Testing image class
class TestImage(TestCase):
    def setUp(self):
        pass

    def test_image_instance(self):
        pass

    def test_image_info(self):
        pass

    def test_image_update(self):
        pass

    def test_image_id(self):
        pass

    def search_image(self):
        pass

    def test_search_by_title(self):
        pass
