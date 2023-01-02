from django.urls import path
from .views import TestApiView,NotAuthen
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/',TestApiView.as_view(), name='test'),
    path('not-authen/',NotAuthen.as_view(), name='not_authen'),
]