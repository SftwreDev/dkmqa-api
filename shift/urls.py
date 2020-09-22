from django.urls import path


from .views import (
    shift_code_list_and_create,
    shift_code_edit_and_delete,
    shift_list_and_create,
    shift_edit_and_delete
)

urlpatterns = [
    path('api/shift-code/', shift_code_list_and_create, name='shift_code_list_and_create' ),
    path('api/shift-code/<int:pk>/', shift_code_edit_and_delete, name='shift_code_edit_and_delete' ),
    path('api/shift/', shift_list_and_create, name='shift_list_and_create' ),
    path('api/shift/<int:pk>/', shift_edit_and_delete, name='shift_edit_and_delete' ),
]
