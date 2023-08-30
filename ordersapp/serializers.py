from typing import Literal
from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    serializer for Order model
    """

    status = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        fields: tuple[
            Literal["parcel_serial_number"],
            Literal["client"],
            Literal["status"],
            Literal["arrival_from"],
            Literal["destination_to"],
            Literal["length"],
            Literal["width"],
            Literal["weight"],
            Literal["time_update"],
        ] = (
            "parcel_serial_number",
            "client",
            "status",
            "arrival_from",
            "destination_to",
            "length",
            "width",
            "weight",
            "time_update",
        )
