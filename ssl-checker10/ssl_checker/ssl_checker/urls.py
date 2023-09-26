from django.contrib import admin
from django.urls import path, include
from ssl_checker_app import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ssl_checker_app/', views.index, name='index'),
    path('check_ssl/', views.check_ssl, name='check_ssl'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name="home.html"), name="home"),
    path('ssl_data/',  views.ssl_data_view, name="ssl_data"),
    path('films/',  views.video_list, name="films"),
    path('videos/play/<str:video_name>/',views.play_video, name='play_video'),
    path('profil/', views.user_profile, name='user_profile'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('ssl_checker_app.urls')),
    path('ssl2/', views.ssl2, name='ssl2'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)