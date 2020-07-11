
from django.contrib import admin
from django.urls import path
from tienda import views as tienda_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', tienda_views.home),
]
