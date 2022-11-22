from django.db import models
from common.models import CommonModel

# Create your models here.
class Experience(CommonModel):
    name = models.CharField(max_length=250)
    country = models.CharField(
        max_length=50,
        default="Korea, Republic of",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="experience",
    )
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
        related_name="experience",
    )

    def __str__(self) -> str:
        return self.name

    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="experience",
    )


class Perk(CommonModel):
    # included feature
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=250, blank=True, default="")
    explanation = models.TextField(blank=True, default="")

    def __str__(self) -> str:
        return self.name
