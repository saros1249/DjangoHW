from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users import views

urlpatterns = [
    path("", views.UserListView.as_view(), name='user'),
    path("create/", views.UserCreateView.as_view(), name='create_user'),
    path("<int:pk>/update/", views.UserUpdateView.as_view(), name='update_user'),
    path("<int:pk>/delete/", views.UserDeleteView.as_view(), name='delete_user'),
    path("<int:pk>/", views.UserDetailView.as_view(), name='user_detail'),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
