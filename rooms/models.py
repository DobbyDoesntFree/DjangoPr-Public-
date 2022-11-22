from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    # Room model definitions
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(max_length=180, default="")
    country = models.CharField(
        max_length=50,
        default="Korea, Republic of",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    descriptions = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(  # many to one (one owner can have several rooms)
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        # many to many (room1, room2, room3) => each room can have => (amenity1, amenity2, amenity3)
        # Ex) room1,2,3,4,5 can have kitchen, dryer
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self):
        return self.name


class Amenity(CommonModel):
    # Amenity definitions

    name = models.CharField(max_length=150)
    descriptions = models.CharField(
        max_length=150,
        null=True,  # DB can be null
        blank=True,  # Form can be empty
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
