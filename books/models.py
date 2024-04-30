from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    content=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return self.title