from django.urls import path


from .views import (
    address_list_or_create,
    address_update_or_delete,

    plant_list_or_create,
    plant_update_or_delete
)

app_name = 'plant'

urlpatterns = [
    path('api/address-overview/', address_list_or_create, name='address_list_and_create'),
    path('api/address-overview/<int:pk>/', address_update_or_delete, name='address_update_and_delete'),


    path('api/plant-overview/', plant_list_or_create, name='plant_list_and_create'),
    path('api/plant-overview/<int:pk>/', plant_update_or_delete, name='plant_update_and_delete'),
]
