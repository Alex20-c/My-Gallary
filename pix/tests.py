from django.test import TestCase
from . models import Image,Category,Location
import datetime as dt

# Create your tests here.
class LocationTestClass(TestCase):
  
    # Set up method
    def setUp(self):
        self.kapsabet= Location(name = 'Kapsabet')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kapsabet,Location))

    # Testing Save Method
    def test_save_method(self):
        self.kapsabet.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.pet=Category(name = 'pet')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.pet,Category))    

    # Testing save method
    def test_save_method(self):
        self.pet.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # Testing display saved images
    def test_display_all_objects_method(self):
        self.pet.save_category()
        all_objects = Category.objects.all()
        self.assertEqual(all_objects.categories,'pet')


    def test_get_pix_by_date(self):
        test_date = '2018-12-07'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        pix_by_date = Category.days_pix(date)
        self.assertTrue(len(pix_by_date) == 0)