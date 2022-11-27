from django.urls import path

from ads import views

urlpatterns = [
    path("", views.SelectionListView.as_view(), name='selection'),
    path("create/", views.SelectionCreateView.as_view(), name='create_selection'),
    path("<int:pk>/update/", views.SelectionUpdateView.as_view(), name='update_selection'),
    path("<int:pk>/delete/", views.SelectionDeleteView.as_view(), name='delete_selection'),
    path("<int:pk>/", views.SelectionDetailView.as_view(), name='ad_selection'),
]