from django.db import models

# Create your models here.


class House(models.Model):

    # House Model
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(
        verbose_name="Price per day", help_text="Enter positive number"
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True, help_text="Is this house allow pet?"
    )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):  # this will run everytime when call this class
        return self.name
