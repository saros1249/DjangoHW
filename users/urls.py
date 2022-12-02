from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserDetailView, UserDeleteView, UserUpdateView, UserCreateView, UserListView

urlpatterns = [
    path("", UserListView.as_view(), name='user'),
    path("create/", UserCreateView.as_view(), name='create_user'),
    path("<int:pk>/update/", UserUpdateView.as_view(), name='update_user'),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name='delete_user'),
    path("<int:pk>/", UserDetailView.as_view(), name='user_detail'),
    path("login/", views.obtain_auth_token, name="login_user"),
    path("token/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
