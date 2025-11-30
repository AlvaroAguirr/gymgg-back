from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/auth/',include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/auth/token/refresh/', TokenRefreshView().as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView().as_view(), name='token_verify'),

    path('products/', include('products.urls')),
    path('products/categories/', include('products.urls')),
    path('membership/', include('membership.urls')),
    path('Sales/', include('sales.urls')),
    path('useraccount/', include('useraccount.urls')),
    path('profile/', include ('client_profile.urls'))
]
