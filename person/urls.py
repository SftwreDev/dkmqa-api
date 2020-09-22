from django.urls import path

from .views import(
    person_list_or_create,
    person_update_or_delete
)

app_name = 'person'

urlpatterns = [
    path('api/person-overview/', person_list_or_create, name = 'person_list_and_create'),
    path('api/person-overview/<int:pk>/', person_update_or_delete, name = 'person_update_and_delete'),
]
