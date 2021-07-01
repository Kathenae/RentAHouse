from django.urls import path
from . import views


urlpatterns = [
    # Base Views
    path('', views.HomeView.as_view(), name='home'),
    path('casas/', views.HousesListView.as_view(), name="house_list"),
    path('casa<int:pk>/', views.HouseDetailView.as_view(), name="house_detail"),
    path('submeter_casa/', views.HouseCreateView.as_view(),name="house_create"),
]
