from django.db import models
from django.conf import settings

from message.models import Message


User = settings.AUTH_USER_MODEL

class Inbox(models.Model):
    last_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='inboxes', blank=True, null=True)
    user = models.ManyToManyField(User, related_name='users', through='Inbox_participants')

class Inbox_participants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE)
