from django.urls import path, include


from . views import (
   
    Category2API, 
    category2,
    
)


urlpatterns = [
 
    path('api/checklist/', Category2API, name='category2_list'),
    path('api/checklist/<int:pk>/', category2, name='create_category2'),
   

]

