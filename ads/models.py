from django.db import models

from users.models import User, Location


class Categories(models.Model):
    name = models.CharField(verbose_name="Название категории объявления", max_length=30, unique=True)

    class Meta:
        verbose_name = "Категория объявления"
        verbose_name_plural = "Категории объявлений"

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='ad')
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=2000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, on_delete=models.SET_NULL, related_name='ad')

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name
