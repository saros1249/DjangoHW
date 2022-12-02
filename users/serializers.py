from datetime import date

from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from users.models import User, Location


def age_new_user_validator(value):
    if relativedelta(date.today(), value).years() < 9:
        raise ValidationError("Возраст меньше 9 лет.")


def validate_email(value):
    if "rambler.ru" in value:
        raise ValidationError("Pегистрация с домена rambler.ru запрещена.")


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "role", "age", "location"]


class UserRetrieveSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "role", "age", "location"]


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all()), validate_email])

    birth_date = serializers.DateTimeField(validators=[age_new_user_validator])

    class Meta:
        model = User
        fields = "__all__"

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)

        loc, _ = Location.objects.get_or_create(name=self._locations)
        user.location = loc
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["password", "first_name", "last_name", "location"]

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save()
        loc, _ = Location.objects.get_or_create(name=self._locations)
        user.location = loc
        user.save()
        return user


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]
