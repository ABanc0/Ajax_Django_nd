from rest_framework import serializers
from ssl_checker_app.models import SSLCertificate
class SSLCertificateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SSLCertificate
        fields=['id','domain','valid_until']
