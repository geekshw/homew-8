from django.db import models

# Create your models here.

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    caption = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.caption or 'No caption' 

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
