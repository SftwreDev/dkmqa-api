from django.urls import path


from . views import (
    Category1API,
    Category2API,
    Category3API,
    category1,
    category2,
    category3,
)


urlpatterns = [
                        
                        ### Category 1 ###
    path('api/category/', Category1API, name='category1_list'),
    path('api/category/<int:pk>/', category1, name='update_category1'),

                        ### Checklist ###
    path('api/checklist/', Category2API, name='category2_list'),
    path('api/checklist/<int:pk>/', category2, name='create_category2'),
   
   
                        ### Defect Codes ###
    path('api/defect-codes/', Category3API, name='category3_list'),
    path('api/defect-codes/<int:pk>/', category3, name='delete_category3'),
]
