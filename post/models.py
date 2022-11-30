from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    heading = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    title_image = models.ImageField(upload_to='photos/', blank=True)
    image_2 = models.ImageField(upload_to='photos/', blank=True)
    image_3 = models.ImageField(upload_to='photos/', blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.heading
    
    def get_url(self):
        return reverse('post_details', args = [self.post_category.slug, self.slug])

class WelcomeNote(models.Model):
    heading = models.TextField(max_length=200)
    
    def __str__(self):
        return self.heading
    