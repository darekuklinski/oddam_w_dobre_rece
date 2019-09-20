from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    Name = models.CharField(max_length=256)

class Institution(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField
    FUNDACJA = 'FN'
    ORGANIZACJA_POZARZADOWA = 'OP'
    ZBIORKA_LOKALNA = 'ZL'
    TYPE_CHOICES = [
        (FUNDACJA, 'fundacja'),
        (ZBIORKA_LOKALNA, 'zbiórka lokalna'),
        (ORGANIZACJA_POZARZADOWA, 'organizacja pozarządowa'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=FUNDACJA
    )
    categories = models.ManyToManyField(Category)

class Fundation(models.Model):
    quantity = models.IntegerField
    categories = models.ManyToManyField(Category)
    institution = models.ManyToManyField(Institution)
    address = models.CharField(max_length=256)
    phone_number = models.IntegerField
    city = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField
    pick_up_time = models.TimeField
    pick_up_comment =  models.TextField
    user = models.ForeignKey(User, on_delete=models.CASCADE)