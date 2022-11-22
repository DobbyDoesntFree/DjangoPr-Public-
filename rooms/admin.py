from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "owner",
        "created_at",
    )
    list_filter = (
        "name",
        "city",
        "price",
        "rooms",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )

    def total_amenities(self, room):
        # print(self) rooms.RoomAdmin
        # print(room) room name (__str__)
        return room.amenities.count()
        # room에 올게 뭔지 모르겠다면 dir 사용 (모델명을 자동으로 lowercase로 바꿔서 _set 달아줌)
        # 혹은 모델명을 소문자로 적어도 됨


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "descriptions",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
