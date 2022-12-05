from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError

from HW27.settings import USER_MIN_AGE


def age_new_user_validator(value):
    diff_date = relativedelta(date.today(), value).years
    if diff_date < USER_MIN_AGE:
        raise ValidationError("Возраст меньше 9 лет.")
    return value


class Location(models.Model):
    name = models.CharField(null=True, max_length=50)
    lat = models.DecimalField(null=True, max_digits=8, decimal_places=6)
    lng = models.DecimalField(null=True, max_digits=8, decimal_places=6)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    def __str__(self):
        return self.name


class UserRole:
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (('Пользователь', USER),
               ('Админ', ADMIN),
               ('Модератор', MODERATOR))


class User(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default='member', max_length=20)
    age = models.PositiveIntegerField(null=True)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    birth_date = models.DateField(validators=[age_new_user_validator])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
