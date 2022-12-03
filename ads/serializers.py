from ads.models import Categories, Ads, Selection
from rest_framework import serializers
from users.models import User


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class AdsListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ads
        fields = "__all__"


class AdsRetrieveSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ads
        fields = "__all__"


class AdsCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ads
        exclude = ["image"]

    def is_valid(self, raise_exception=False):
        self.initial_data._mutable = True
        self._author = self.initial_data.pop("author")
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ads = Ads.objects.create(**validated_data)
        author, _ = User.objects.get_or_create(username=self._author)
        ads.author = author
        ads.save()
        return ads


class AdsUpdateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        required=False,
        queryset=Categories.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Ads
        exclude = ["image"]

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop("author")
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        ads = super().save()
        author, _ = User.objects.get_or_create(username=self._author)
        ads.author = author
        ads.save()
        return ads


class AdsDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = "id"


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionRetrieveSerializer(serializers.ModelSerializer):
    items = AdsListSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["name", "items"]

    def is_valid(self, raise_exception=False):
        self._items = self.initial_data.pop("items", [])
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        selection = super().save()

        for item in self._items:
            selection.items.add(item)
        selection.save()
        return selection


class SelectionDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "id"
