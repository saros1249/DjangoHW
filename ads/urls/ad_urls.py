from django.urls import path

from ads import views

urlpatterns = [
    path("", views.AdsListView.as_view(), name='ad'),
    path("create/", views.AdsCreateView.as_view(), name='create_ad'),
    path("<int:pk>/update/", views.AdsUpdateView.as_view(), name='update_ad'),
    path("<int:pk>/delete/", views.AdsDeleteView.as_view(), name='delete_ad'),
    path("<int:pk>/", views.AdsDetailView.as_view(), name='ad_detail'),
    path("<int:pk>/upload_image/", views.AdsImageView.as_view(), name="upload_image"),
]