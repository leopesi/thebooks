from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalogo.urls')),
    path('', include("catalogo.authentication.urls")),  # Auth routes - login / register
    #path('', include("catalogo.home.urls"))  # UI Kits Html files
]
