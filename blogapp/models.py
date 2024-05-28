from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.title