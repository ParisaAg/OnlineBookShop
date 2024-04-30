from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    content=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=5)
    def __str__(self):
        return f'{self.title} by : {self.author}'

    def get_absolute_url(self):
        return reverse('book_detail',args=[self.id])
