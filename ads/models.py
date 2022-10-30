from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
