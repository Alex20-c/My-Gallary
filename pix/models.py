from django.db import models
import datetime as dt


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()
    
    class Meta:
        ordering = ['first_name']
        verbose_name = 'Editor'
        verbose_name_plural = 'Editors'
class tags(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def save_category(self):
        self.save()
        
    def __str__(self):
        return self.name
        
class Location(models.Model):
    name = models.CharField(max_length=50)

    def save_location(self):
        self.save()
        
    def __str__(self):
        return self.name


class Image(models.Model):
    image_path = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=60)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def days_pix(cls,date):
        pix = cls.objects.filter(pub_date__date = date)
        return pix

    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(category__name__icontains=search_term)
        return search_result

    @classmethod
    def image_category(cls,category):
        image = cls.objects.filter(category = category)

        return image
