# Generated by Django 4.1.2 on 2022-11-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="House",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=140)),
                (
                    "price",
                    models.PositiveIntegerField(
                        help_text="Enter positive number", verbose_name="Price per day"
                    ),
                ),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=140)),
                (
                    "pets_allowed",
                    models.BooleanField(
                        default=True, help_text="Is this house allow pet?"
                    ),
                ),
            ],
        ),
    ]
