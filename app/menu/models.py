from django.db import models

# Create your models here.


class IceCream(models.Model):

    name = models.CharField(max_length=100)

    # image = models.ImageField()

    type = models.CharField(max_length=100)

    description = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.type}'
