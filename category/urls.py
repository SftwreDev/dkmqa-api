from django.urls import path, include


from . views import (
    Category1API,
    category1,
   
)


urlpatterns = [
                        
                        ### Category 1 ###
    path('api/category/', Category1API, name='category1_list'),
    path('api/category/<int:pk>/', category1, name='update_category1'),


]

