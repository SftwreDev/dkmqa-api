from django.urls import path, include
from knox import views as knox_views
from rest_framework_simplejwt import views as jwt_views

from .views import (
    RegisterAPI,
    LoginAPI,
    # ExampleView,
)

app_name = 'api'

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    # path('api/register/', RegisterAPI.as_view(), name='api_register'),
    # path('api/login/', LoginAPI.as_view(), name='api_login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='api_logout'),
    # path('api/logout-all/', knox_views.LogoutAllView.as_view(), name='api_logout_all'),
    # # path('index/', ExampleView.as_view(), name='try'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    
]

