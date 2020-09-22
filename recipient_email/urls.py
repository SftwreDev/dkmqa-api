from django.urls import path


from .views import (
    email_list_and_create,
    email_edit_and_delete
)

urlpatterns = [
    path('api/recipient-email/', email_list_and_create, name = 'email_list_and_create'),
    path('api/recipient-email/<int:pk>/', email_edit_and_delete, name = 'email_edit_and_delete'),
]
