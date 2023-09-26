from django.shortcuts import render
from django.http import JsonResponse
from .models import SSLCertificate
import ssl
import socket
import datetime
import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import VideoSearchForm
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from rest_framework import viewsets
from ssl_checker_app.models import SSLCertificate
from ssl_checker_app.serializer import SSLCertificateSerializer
import requests

class SSLCertificateViewSet(viewsets.ModelViewSet):
    queryset = SSLCertificate.objects.all()
    serializer_class = SSLCertificateSerializer

@login_required
def ssl2(request):
    api_url = "http://192.168.88.91:8000/api/api/LSS/"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            
            data = response.json()
            data = sorted(data, key=lambda x:x['id'],reverse=True)
            context = {'data': data}
            return render(request, 'ssl_datastronaosxka.html', context)
        else:
            error_message = f"Nie udało się pobrać danych. Kod odpowiedzi: {response.status_code}"
            return render(request, 'error.html', {'error_message': error_message})

    except Exception as e:
        error_message = f"Wystąpił błąd: {str(e)}"
        return render(request, 'error.html', {'error_message': error_message})
class CustomLoginView(LoginView):
    template_name = 'login.html' 

def user_profile(request):

    user = request.user

    return render(request, 'user_profile.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało utworzone dla {username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profil użytkownika został zaktualizowany!')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'profile.html', {'profile_form': profile_form})



def video_list(request):
    media_folder = 'media'
    video_files = [f for f in os.listdir(media_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]
    videos = [{'title': os.path.splitext(video)[0], 'file': f'/{media_folder}/{video}'} for video in video_files]

    form = VideoSearchForm(request.GET)
    search_query = request.GET.get('search_query', '')
    clear_search = request.GET.get('clear_search', '')

    if clear_search:
        search_query = ''
        form = VideoSearchForm()

    if search_query:
        videos = [video for video in videos if search_query.lower() in video['title'].lower()]

    return render(request, 'films.html', {'videos': videos, 'form': form, 'search_query': search_query})

def play_video(request, video_name):
    video_path = os.path.join(settings.MEDIA_URL, video_name)
    return render (request, 'play_video.html', {'video_path': video_path})

def ssl_data_view(request):
    certificates = SSLCertificate.objects.all().order_by('-created_at')
    return render (request, 'ssl_data.html', {'certificates': certificates})

def index(request):
    return render(request, 'index.html')

def check_ssl(request):
    if request.method == 'POST':
        domain = request.POST.get('domain')
        try:
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert(binary_form=True)

            x509_cert = x509.load_der_x509_certificate(cert, default_backend())
            cert_end_date = x509_cert.not_valid_after
            days_left = (cert_end_date - datetime.datetime.now()).days

            ssl_cert = SSLCertificate.objects.create(
                domain=domain,
                valid_until=cert_end_date,
            )
            ssl_cert.save()

            response_data = {
                'success': True,
                'domain': domain,
                'valid_until': cert_end_date.strftime('%Y-%m-%d'),
                'days_left': days_left
            }
        except Exception as e:
            response_data = {
                'success': False,
                'message': str(e)
            }
        return JsonResponse(response_data)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})

