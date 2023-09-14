from django.urls import path, include
from . import views

urlpatterns = [
    path('ssl_checker_app/', views.index, name='index'),
    path('check_ssl/', views.check_ssl, name='check_ssl'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('home/', views.home, name='home'),
    path('ssl_data/', views.ssl_data_view, name="ssl_data" )
]

