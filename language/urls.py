from django.urls import path

from .views import (
    language_list_and_create,
    language_update_and_delete
)


urlpatterns = [
    path('api/language/' , language_list_and_create, name = 'language_list_and_create'),
    path('api/language/<int:pk>/' , language_update_and_delete, name = 'language_update_and_delete'),
]
