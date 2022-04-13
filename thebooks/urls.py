from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalogo.api import viewsets as booksviewsets
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'api', booksviewsets.BooksViewSet, basename='api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('', include('catalogo.urls')),
    path('', include("catalogo.authentication.urls")),  # Auth routes - login / register
    path('', include("catalogo.home.urls"))  # UI Kits Html files
]
