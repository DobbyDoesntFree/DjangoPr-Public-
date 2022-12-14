# Generated by Django 4.1.2 on 2022-11-07 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_alter_amenity_options_amenity_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="amenity",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="amenity",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="room",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
