from django.urls import path, include
from knox import views as knox_views

from .views import (
    RegisterAPI,
    LoginAPI,
    # ExampleView,
)

app_name = 'api'

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='api_register'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='api_logout'),
    path('api/logout-all/', knox_views.LogoutAllView.as_view(), name='api_logout_all'),
    # path('index/', ExampleView.as_view(), name='try'),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]

