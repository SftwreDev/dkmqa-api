from django.urls import path

from . views import (

    Category3API,
    category3,
    defect_codes_translation,
    defect_codes_translation_edit_and_delete

)


urlpatterns = [

                        ### Defect Codes ###
    path('api/defect-codes/', Category3API, name='category3_list'),
    path('api/defect-codes/<int:pk>/', category3, name='delete_category3'),

                        ### Defect Codes Translation ###
    path('api/defect-codes-translations/', defect_codes_translation, name='defect_codes_translation'),
    path('api/defect-codes-translations/<int:pk>/', defect_codes_translation_edit_and_delete, name='defect_codes_translation_edit_and_delete'),
]

