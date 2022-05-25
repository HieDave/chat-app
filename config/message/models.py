from django.db import models
from django.conf import settings

import inbox


User = settings.AUTH_USER_MODEL

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    inbox = models.ForeignKey("inbox.Inbox", on_delete=models.CASCADE)