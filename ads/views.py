import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from HW27 import settings
from ads.models import Ads, Categories
from users.models import User


def index(request):
    return JsonResponse({"status": "ok"}, status=200)



class CatListView(ListView):

    def get(self, request, *args, **kwargs):
        cat_list = Categories.objects.all()

        response = []
        for cat in cat_list:
            response.append({
                "id": cat.id,
                "name": cat.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CatCreateView(CreateView):
    model = Categories
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)

        cat = Categories.objects.create(name=cat_data["name"])

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CatUpdateView(UpdateView):
    model = Categories
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)

        self.object.name = cat_data["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        }, safe=False, json_dumps_params={"ensure_ascii": False})


class CatDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted successfully"}, status=200)


class CatDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


class AdsListView(ListView):
    model = Ads
    queryset = Ads.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(self, *args, **kwargs)

        self.object_list = self.object_list.order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)

        ads_list = []
        for ads in page_object:
            ads_list.append({
                "id": ads.id,
                "name": ads.name,
                "author": ads.author_id,
                "price": ads.price,
                "description": ads.description,
                "is_published": ads.is_published,
                "image": str(ads.image),
                "category": ads.category_id
            })

        response = {
            "items": ads_list,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads
    fields = ["name", "author_id", "price", "description", "is_published", "image", "category_id"]

    def post(self, request, *args, **kwargs):
        ads_data = json.loads(request.body)

        ads = Ads.objects.create(
            name=ads_data["name"],
            price=ads_data["price"],
            description=ads_data["description"]
        )

        ads.user = get_object_or_404(User, pk=ads_data["user_id"])
        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published
        }, json_dumps_params={"ensure_ascii": False})

@method_decorator(csrf_exempt, name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads
    fields = ["name", "price", "description"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ads_data = json.loads(request.body)

        self.object.name = ads_data["name"]
        self.object.price = ads_data["price"]
        self.object.description = ads_data["description"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
        }, safe=False, json_dumps_params={"ensure_ascii": False})

@method_decorator(csrf_exempt, name="dispatch")
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted successfully"}, status=200)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ads = self.get_object()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author.first_name,
            "price": ads.price,
            "description": ads.description,
            "address": ads.ad.location_id.name,
            "is_published": ads.is_published
        })
@method_decorator(csrf_exempt, name="dispatch")
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
