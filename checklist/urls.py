from django.urls import path, include


from . views import (
   
    Category2API, 
    category2,
    translation_list_and_create,
    translation_update_and_delete    
)


urlpatterns = [
    
    ############ URL For Checklist API ############

    path('api/checklist/', Category2API, name='category2_list'),
    path('api/checklist/<int:pk>/', category2, name='create_category2'),
   
   ############ URL For Checklist Translation API ############

    path('api/checklist-translation/', translation_list_and_create, name='translation_list_and_create'),
    path('api/checklist-translation/<int:pk>/', translation_update_and_delete, name='translation_update_and_delete'),
]

