from django.contrib import admin
from .models import Inbox, Inbox_participants

# Register your models here.
admin.site.register(Inbox)
admin.site.register(Inbox_participants)