from django.urls import path


from .views import (
    address_list_or_create,
    address_update_or_delete,

    plant_list_or_create,
    plant_update_or_delete,
    Webhooks
)

app_name = 'plant'

urlpatterns = [
    path('hub.mode=<str:mode>&hub.verify_token=<str:token>&hub.challenge=<str:challenge>', Webhooks, name='webhooks_verify'),
]
