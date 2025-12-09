from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from dj_rest_auth.views import LoginView, LogoutView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
schema_view = get_schema_view(
   openapi.Info(
      title="GymGG API",
      default_version='v1',
      description="API para GymGG",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/auth/',include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/auth/token/refresh/', TokenRefreshView().as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView().as_view(), name='token_verify'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 

    path('products/', include('products.urls')),
    # path('products/categories/', include('products.urls')),
    path('membership/', include('membership.urls')),
    path('Sales/', include('sales.urls')),
    path('useraccount/', include('useraccount.urls')),
    path('profile/', include ('client_profile.urls')),
    path('routines/', include('routines.urls')),
]
