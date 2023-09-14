from django.db import models

# Create your models here.


class Micdejun(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='image/', null=True)
    ingredients = models.TextField(max_length=500)
    small_description = models.TextField(max_length=500)
    mod_preparare = models.TextField(max_length=2000)
