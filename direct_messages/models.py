from django.db import models
from common.models import CommonModel

# Create your models here.


class ChatRoom(CommonModel):
    users = models.ManyToManyField(
        "users.User",  # user, chatroom able to many to many rel
    )  # can cause problem since same classname connected to users.User model
    # same classname itself dosen't matter
    def __str__(self):
        return "Chatting Room"


class Message(CommonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    chatroom = models.ForeignKey(
        "direct_messages.ChatRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.user} says : {self.text}"
