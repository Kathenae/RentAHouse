from django.urls import path
from . import views


urlpatterns = [
    # Base Views
    path('', views.HomeView.as_view(), name='home'),
    path('casas/', views.HousesListView.as_view(), name="house_list"),
    path('casa<int:pk>/', views.HouseDetailView.as_view(), name="house_detail"),
    path('casa<int:pk>/alterar/', views.HouseUpdateView.as_view(), name="house_update"),
    path('casas<int:pk>/eliminar/', views.HouseDeleteView.as_view(), name="house_delete"),
    path('casa<int:listing_pk>/upload/', views.upload_listing_picture, name="house_upload"),
    path('casas/submeter/', views.HouseCreateView.as_view(),name="house_create"),
    path('casas/minhas-casas/', views.UserHouseListView.as_view(), name="house_user_houses"),
]
