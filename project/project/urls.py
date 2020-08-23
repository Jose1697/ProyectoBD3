
from django.contrib import admin
from django.urls import path
from tienda import views as tienda_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', tienda_views.home, name='home'),
    path('signup/',tienda_views.signup,name='registro'),
    path('login/',tienda_views.login_view,name='login'),
    path('logout/',tienda_views.logout_view,name='logout'),
    path('reclamo/',tienda_views.reclamo,name='reclamo')
]
