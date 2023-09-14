from django.db import models

# Create your models here.


class Cina(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', null=True)
    ingredients = models.TextField(max_length=500)
    description = models.TextField(max_length=500)
