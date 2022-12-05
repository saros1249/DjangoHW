from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from users.models import User, Location


class Categories(models.Model):
    slug = models.CharField(unique=True, max_length=10, validators=[MinLengthValidator(5)])
    name = models.CharField(verbose_name="Название категории объявления", max_length=30, unique=True)

    class Meta:
        verbose_name = "Категория объявления"
        verbose_name_plural = "Категории объявлений"

    def __str__(self):
        return self.name


class Ads(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
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


class Selection(models.Model):
    name = models.CharField(max_length=50, null=False)
    owner = models.IntegerField(null=True)
    items = models.ManyToManyField(Ads)

    class Meta:
        verbose_name = "Подборка объявлений"
        verbose_name_plural = "Подборки объявлений"

    def __str__(self):
        return self.name
