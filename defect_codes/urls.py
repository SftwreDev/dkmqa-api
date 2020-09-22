from django.urls import path

from . views import (

    Category3API,
    category3,
)


urlpatterns = [

                        ### Defect Codes ###
    path('api/defect-codes/', Category3API, name='category3_list'),
    path('api/defect-codes/<int:pk>/', category3, name='delete_category3'),


]

