from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category (models.Model):
    category_name =  models.CharField(max_length=40)
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
    
STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('Published', 'Published')
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=2000)
    blog_body = models.TextField(max_length=2000)
    status = models.TextField(choices=STATUS_CHOICES, default=0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


