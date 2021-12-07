from django.db import models


class Message(models.Model):
    user_id = models.IntegerField(max_length=10)
    chat_message = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.chat_message}"
