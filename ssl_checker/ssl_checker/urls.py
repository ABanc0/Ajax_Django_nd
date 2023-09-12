from django.contrib import admin
from django.urls import path, include
from ssl_checker_app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('check_ssl/', views.check_ssl, name='check_ssl'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]