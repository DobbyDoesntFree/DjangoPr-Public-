from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "Male")  # ('value for db', 'value for adminpage')
        FEMALE = ("female", "Female")  # value for db must be match maxlength condition

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        KRW = "krw", "Korea Won"
        USD = "usd", "US Dollar"

    first_name = models.CharField(
        ("first name"),
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        ("last name"),
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    avatar = models.ImageField(blank=True)  # need Pillow
    is_host = models.BooleanField(default=False)  # or null=True
    gender = models.CharField(
        max_length=10,
        choices=GenderChoice.choices,
        default="male",
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default="kr",
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
        default="krw",
    )
