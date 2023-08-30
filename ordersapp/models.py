import uuid
from django.db import models


class Order(models.Model):
    """
    Orders model
    """

    STATUS_OF_PARCEL = [("1", "New"), ("2", "Placed"), ("3", "Given"), ("4", "Refusal")]

    parcel_serial_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    client = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_OF_PARCEL, default="New")
    length = models.IntegerField(verbose_name="Length, cm")
    width = models.IntegerField(verbose_name="Width, cm")
    weight = models.IntegerField(verbose_name="Weight, kg")
    arrival_from = models.CharField(max_length=100)
    destination_to = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.parcel_serial_number)

    class Meta:
        ordering = ["-time_update"]
