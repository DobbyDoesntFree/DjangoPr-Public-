from django.db import models


# Create your models here.
class CommonModel(models.Model):
    # Common Model definitions

    created_at = models.DateTimeField(
        auto_now_add=True,
    )  # set time as created
    updated_at = models.DateTimeField(
        auto_now=True,
    )  # set time as saved(updated)
    # use datefield if just need yymmdd
    class Meta:  # use this if this model Dosen't need to add to DB
        abstract = True
