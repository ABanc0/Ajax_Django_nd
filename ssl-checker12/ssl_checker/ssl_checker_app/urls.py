from django.urls import path, include
from . import views
from rest_framework import routers
from ssl_checker_app.views import SSLCertificateViewSet


router=routers.DefaultRouter()
router.register(r'SSL', SSLCertificateViewSet)


urlpatterns = [
    path('ssl_checker_app/', views.index, name='index'),
    path('check_ssl/', views.check_ssl, name='check_ssl'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('ssl_data/', views.ssl_data_view, name="ssl_data" ),
    path('films/',  views.video_list, name="films"),
    path('videos/play/<str:video_name>/',views.play_video, name='play_video'),
    path('profil/', views.user_profile, name='user_profile'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('api/', include(router.urls)),
    path('ssl2/', views.ssl2, name='ssl2'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('photos/', views.lista_zdjec, name='lista_zdjec'),

]

