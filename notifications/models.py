from django.db import models

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications_sent') 
    verb = models.CharField(max_length=255)
    target_ct = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE) 
    target_id = models.PositiveIntegerField(null=True, blank=True) 
    target = GenericForeignKey('target_ct', 'target_id') 
    read = models.BooleanField(default=False) 
    timestamp = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['recipient', 'read']),
        ]

    def __str__(self):
        if self.target:
            return f"{self.actor.username} {self.verb} {self.target}"
        return f"{self.actor.username} {self.verb}"