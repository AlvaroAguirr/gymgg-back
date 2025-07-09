from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
  
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('products/categories/', include('products.urls')),
    path('membership/', include('membership.urls')),
    path('Sales/', include('sales.urls')),
    path('useraccount/', include('useraccount.urls')),
]
