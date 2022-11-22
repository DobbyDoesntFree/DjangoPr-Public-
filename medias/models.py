from django.db import models
from common.models import CommonModel

# Create your models here.


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photo",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photo",
    )

    def __str__(self) -> str:
        return "PHOTO FILE"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(  # by this the experiences can't have more Video
        # this maening experience able to have only one video
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="video",
    )

    def __str__(self) -> str:
        return "VIDEO FILE"
