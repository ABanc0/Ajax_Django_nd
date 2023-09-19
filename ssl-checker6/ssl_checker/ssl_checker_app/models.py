from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class SSLCertificate(models.Model):
    id = models.AutoField(primary_key=True)
    domain = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    valid_until = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.domain

def default_profile_picture():
    return 'profile_pics/image2.png'

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True , null=True, default=default_profile_picture)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()