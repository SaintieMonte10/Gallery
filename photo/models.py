# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
    
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    loc_name = models.CharField(max_length=30)
    
    def save_loc(self):
        self.save()
        
    def delete_loc(self):
        self.delete()
    
    def __str__(self):
        return self.loc_name
      
class Image(models.Model):
    image = models.ImageField(upload_to='photos/')
    image_name = models.CharField(max_length=30)
    image_descprition = models.CharField(max_length=150)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.get(id = id)
        
        return image
    @classmethod
    def search_image(cls,categorys):
        images = cls.objects.filter(category__name = categorys)
        
        return images
    
    @classmethod
    def filter_by_location(cls,location):
        
        images_locs = cls.objects.filter(location__loc_name=location)
        
        return images_locs
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']
   