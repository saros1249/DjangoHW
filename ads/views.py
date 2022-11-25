from ads.serializers import *
from django.db.models import Q
from django.http import JsonResponse

from django.views.generic import UpdateView

from ads.models import Ads, Categories
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class CatViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CatSerializer


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsListSerialiser

    def get(self, request, *args, **kwargs):

        ad_cat = request.GET.get("cat", None)
        if ad_cat:
            self.queryset = self.queryset.filter(
                category__id__icontains=ad_cat
            )

        ad_name = request.GET.get("name", None)
        if ad_name:
            self.queryset = self.queryset.filter(
                name__icontains=ad_name
            )

        ad_location = request.GET.get("location", None)
        if ad_location:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=ad_location
            )

        ad_prise_min = request.GET.get("price_from", None)
        ad_prise_max = request.GET.get("price_to", None)
        if ad_prise_min and ad_prise_max:
            self.queryset = self.queryset.filter(
                Q(price__gte=ad_prise_min) & Q(price__lte=ad_prise_max)
            )

        return super().get(request, *args, **kwargs)


class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsRetrieveSerializer


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer


class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer


class AdsDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsDestroySerializer


class AdsImageView(UpdateView):
    model = Ads
    fields = ["image"]

    def patch(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author,
            "price": self.object.price,
            "description": self.object.description,
            "address": self.object.address,
            "is_published": self.object.is_published,
            "image": self.object.image
        }, safe=False, json_dumps_params={"ensure_ascii": False})
