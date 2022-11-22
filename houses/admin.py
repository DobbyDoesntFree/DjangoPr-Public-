from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # pass
    fields = (
        "name",
        "price",
        ("address", "pets_allowed"),
        "owner",
    )
    list_display = ("name", "price", "address", "pets_allowed")  # show element in list

    list_filter = ("name", "price", "address", "pets_allowed")  # select search terms

    search_fields = (
        "address__startswith",
    )  # add comma. if not, VSC treat it as string
    # exclude=("price",)  block modify in admin page

    list_display_links = (
        "name",
        "address",
    )  # grant enterance point to manage panel

    list_editable = (
        "pets_allowed",
    )  # make modify contents in list (not in manage panel)
