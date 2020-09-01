from django.urls import path


from . views import (
    Category1API,
    category1_create_api,
    update_category1_api, 
    delete_category1_api,
    Category2API,
    category2_create_api,
    delete_category2_api,
    Category3API,
    category3_create_api,
    delete_category3_api
)


urlpatterns = [
    
    path('api/category/', Category1API.as_view(), name='category1_list'),
    path('api/category-label/', category1_create_api, name='create_category1'),
    path('api/category-label/<int:pk>/', update_category1_api, name='update_category1'),
    path('api/category-label/<int:pk>/', delete_category1_api, name='delete_category1'),
    path('api/checklist/', Category2API.as_view(), name='category2_list'),
    path('api/checklist/create', category2_create_api, name='create_category2'),
    path('api/checklist/<int:pk>/', delete_category2_api, name='delete_category2'),
    path('api/defect-codes/', Category3API.as_view(), name='category3_list'),
    path('api/defect-codes/add/', category3_create_api, name='create_category3'),
    path('api/defect-codes/<int:pk>/', delete_category3_api, name='delete_category3'),
]
