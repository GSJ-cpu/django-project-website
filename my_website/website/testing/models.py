from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)

class Data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.first_name

class Exhibit(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    age_rec = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    desc = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    subjects = models.CharField(max_length=100)

    def __str__(self):
        return self.title