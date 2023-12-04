from django.contrib import admin
from django.urls import path, include
from mybooks_api import urls as mybooks_urls

urlpatterns = [
    path('admin/', admin.site.urls), # admin
    path('api-auth/', include('rest_framework.urls')), # rest framework
    path('api/', include(mybooks_urls)),
]
