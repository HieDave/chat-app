from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.FileField(upload_to='profile/', null=True, blank=True)
    name = models.CharField(max_length=255)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
