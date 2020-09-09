from django.urls import path


from . views import (
    Category1API,
    Category2API,
    Category3API,
    category3_create_api,
    delete_category3_api,
    category1,
    category2,
)


urlpatterns = [
                        
                        ### Category 1 ###
    path('api/category/', Category1API, name='category1_list'),
    path('api/category/<int:pk>/', category1, name='update_category1'),

                        ### Checklist ###
    path('api/checklist/', Category2API, name='category2_list'),
    path('api/checklist/<int:pk>/', category2, name='create_category2'),
   
   
                        ### Defect Codes ###
    path('api/defect-codes/', Category3API.as_view(), name='category3_list'),
    path('api/defect-codes/add/', category3_create_api, name='create_category3'),
    path('api/defect-codes/<int:pk>/', delete_category3_api, name='delete_category3'),
]
