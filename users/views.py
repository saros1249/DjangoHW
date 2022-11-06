import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from HW27 import settings
from users.models import User, Location


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("username")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)

        user_list = []
        for user in page_object:
            user_list.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "role": user.role,
                "ads_count": user.ad.count()

            })

        response = {
            "items": user_list,
            "num_pages": paginator.num_pages,
            "total": paginator.count
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})

@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ["username", "password", "first_name", "last_name", "role", "age"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        ads_user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            age=user_data["age"],
            password=user_data["password"]
        )

        # for loc in user_data["location"]:
        #     user_location = Location.objects.get_or_create(name=loc)
        #
        # ads_user.location_id.add(user_location)
        ads_user.save()

        return JsonResponse({
            "username": ads_user.username,
            "first_name": ads_user.first_name,
            "last_name": ads_user.last_name,
            "role": ads_user.role
        }, json_dumps_params={"ensure_ascii": False})

@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ["password", "first_name", "last_name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.password = user_data["password"]

        # for loc in user_data["location_id"]:
        #     location = Location.objects.get_or_create(name=loc)
        #
        # self.object.location_id.add(location)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            #"location_id": self.object.location_id,
        }, safe=False, json_dumps_params={"ensure_ascii": False})

@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "deleted successfully"}, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "role": user.role,
            "location_id": user.location_id
        })


