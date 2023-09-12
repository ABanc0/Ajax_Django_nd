from django.shortcuts import render
from django.http import JsonResponse
from .models import SSLCertificate
import ssl
import socket
import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from django.contrib.auth.decorators import login_required
@login_required
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