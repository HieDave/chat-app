from django.db import models
from django.conf import settings

from profiles.models import Profile
import inbox



class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    inbox = models.ForeignKey("inbox.Inbox", on_delete=models.CASCADE)

    def __str__(self):
        return self.message_text