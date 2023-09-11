
from django.db import models

class SSLCertificate(models.Model):
    domain = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    valid_until = models.DateField()

    def __str__(self):
        return self.domain
