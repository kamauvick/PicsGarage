import datetime

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
        Category.objects.all().delete()


# Location tests
class Location(TestCase):
    def setUp(self):
        self.new_location = Location(place='Nairobi')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def save_location(self):
        before = Location.objects.count()
        self.new_location.save_location()
        after = Location.objects.count()
        self.assertTrue(before < after)

    def tearDown(self):
        Location.objects.all().delete()


# Testing image class
class TestImage(TestCase):
    def setUp(self):
        self.category = Category(name='cars')
        self.category.save()

        self.location = Location(place='juja')
        self.location.save_location()

        self.new_image = Image(name='Bmw', description='A perfect Bmw', category=self.category, location=self.location,
                               submitted=datetime.date.today(), url='images/bmw.jpg')

    def test_image_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    def test_image_update(self):
        pass

    def test_image_id(self):
        pass

    def test_search_image(self):
        pass

    def test_save_image(self):
        before = Image.objects.count()
        self.new_image.save_image()
        after = Image.objects.count()
        self.assertTrue(before < after)

    def test_search_by_title(self):
        pass

    def tearDown(self):
        Image.objects.all().delete()
