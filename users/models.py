from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=8, decimal_places=6)

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


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(choices=UserRole.choices, default='member', max_length=20)
    age = models.PositiveIntegerField()
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
