from django.db import models

# Create your models here.
class Dish(models.Model):
  name = models.CharField(max_length=100)
  price = models.CharField(max_length=100)
    