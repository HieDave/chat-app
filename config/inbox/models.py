from django.db import models

from message.models import Message
from profiles.models import Profile


class Inbox(models.Model):
    last_message = models.ForeignKey(
        Message, 
        on_delete=models.CASCADE, 
        related_name='inboxes', 
        blank=True, 
        null=True
        )
    profiles = models.ManyToManyField(
        Profile, 
        related_name='inboxes'
        )

    