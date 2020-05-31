# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import *

# Create your tests here.
class LocationTestClass(TestCase):
    
    def setUp(self):
        self.clare = Location(loc_name = 'nakuru', id=1)
        
        
  #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.clare,Location)) 

    def test_save_method(self):
        self.clare.save_loc()
        editors = Location.objects.all()
        self.assertTrue(len(editors)>0)
        
    def test_delete_method(self):
        self.clare.delete_loc()
        locations = Location.objects.all()
        self.assertTrue(len(locations) is 0)
        
    def test_display_all(self):
        jess = Location(loc_name='uganda')
        jess.save_loc()
        self.clare.save_loc()
        locations = Location.objects.all()
        print(len(locations))
        self.assertTrue(len(locations),2)

         
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTestClass(TestCase):
    
    def setUp(self):
        self.category = Category(name = 'jess', id=1)
        
        
  #Testing instance
    
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category)) 

    def test_save_method(self):
        self.category.save_category()
        catego = Category.objects.all()
        self.assertTrue(len(catego)>0)
        
    def test_delete_method(self):
        self.category.delete_category
        cat = Category.objects.all()
        self.assertTrue(len(cat) is 0)
        
    def test_display_all(self):
        jess = Category(name='general')
        jess.save_category()
        one = Category.objects.all()
        print(len(one))
        self.assertTrue(len(one),2)

class ImageTestClass(TestCase):
    
    def setUp(self):
        self.nakuru = Location(loc_name='nakuru')
        self.nature = Category(name='general')
        self.image = Image(image='images/lagoon.jpeg',image_name='jess', image_descprition='she loves photos',location=self.nakuru,category=self.nature, id=1)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image)) 
