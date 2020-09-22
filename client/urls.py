from django.urls import path

from .views import (
    client_list_and_create,
    client_update_and_delete
)

app_name = 'client'

urlpatterns = [
    path('api/client/', client_list_and_create, name = 'client_overview'),
    path('api/client/<int:pk>/', client_update_and_delete, name='client_overview_edit')

]
