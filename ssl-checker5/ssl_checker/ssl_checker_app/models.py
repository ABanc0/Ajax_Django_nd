from django.db import models
from django.utils import timezone
class SSLCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    valid_until = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.domain

