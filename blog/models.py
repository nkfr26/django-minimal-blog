from django.db import models

# Create your models here.
class Post(models.Model):
    slug = models.SlugField()
    title, content = [
        models.CharField(max_length=255),
        models.TextField()
    ]

    def __str__(self):
        return self.title
