from django.urls import path
from . import views


urlpatterns = [
    # Base Views
    path('', views.HomeView.as_view(), name='home'),
    path('casas/', views.HousesListView.as_view(), name="house_list"),
    path('casa<int:pk>/', views.HouseDetailView.as_view(), name="house_detail"),
    path('casa<int:pk>/alterar/', views.HouseUpdateView.as_view(), name="house_update"),
    path('casas<int:pk>/eliminar/', views.HouseDeleteView.as_view(), name="house_delete"),
    path('casa<int:house_pk>/upload/', views.create_compartment, name="create_compartment"),
    path('casa/delete_picture/<int:compartment_pk>/', views.delete_compartment, name="delete_compartment"),
    path('casas/submeter/', views.HouseCreateView.as_view(),name="house_create"),
    path('casas/minhas-casas/', views.UserHouseListView.as_view(), name="house_user_houses"),
    path('casa<int:listing_pk>/mostrar-na-lista/', views.toggle_house_visibility, name="house_toggle_visibility")
]
