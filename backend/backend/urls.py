from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
]
