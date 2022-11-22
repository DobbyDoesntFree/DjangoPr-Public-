from django.db import models
from common.models import CommonModel


# Create your models here.
class Review(CommonModel):
    # Review for experiences, room
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="review",
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="review",
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"
