from django.urls import path

from ads import views

urlpatterns = [
    path("", views.CatListView.as_view(), name='cat'),
    path("create/", views.CatCreateView.as_view(), name='create_cat'),
    path("<int:pk>/update/", views.CatUpdateView.as_view(), name='update_cat'),
    path("<int:pk>/delete/", views.CatDeleteView.as_view(), name='delete_cat'),
    path("<int:pk>/", views.CatDetailView.as_view(), name='cat_detail'),
]