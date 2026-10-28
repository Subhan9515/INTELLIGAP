
from django.db import models


class ChatMessage(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    role = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.role}: {self.message[:50]}"