from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .serializers import OrderSerializer
from .permissions import IsStatusNotNewOrRefusalDoNotUpdate

from .models import Order
from .services import change_status_after_creation, change_status_finally


class OrdersCreateListViewSets(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    Create and List views for getting and making orders
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def task_complete(self) -> None:
        """
        method for running a task after creating post
        """  
        if self.action == "create":
            tasks_run()


class OrdersUpdateView(generics.UpdateAPIView):
    """
    Method for updating orders
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        IsStatusNotNewOrRefusalDoNotUpdate,
    ]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, **self.kwargs)
        self.check_object_permissions(self.request, obj)
        obj.status = "New"
        return obj

    def task_complete(self) -> None:
        """
        method for running a task after getting post updated
        """        
        if self.action == "update":  # type: ignore
            tasks_run()


class OrdersRetrieveViewSet(viewsets.ViewSet):
    """
    Custom class for getting detail data about order
    """

    def retrieve(self, request, pk=None):
        """
        The overrided method for retrieving particular order`s information (serial and status of order)

        Args:
            request : data from request
            pk (uuid, optional): getting uuid/number or order. Defaults to None.

        Raises:
            NotFound: if order by this uuid does not exist

        Returns:
            Json response: returning response unless errors
        """
        uuid = pk
        try:
            order: Order = Order.objects.all().get(parcel_serial_number=uuid)
            serializer = OrderSerializer(order)
            return Response(serializer.data["status"])
        except Order.DoesNotExist:
            raise NotFound(f"Order with parcel serial number {uuid} not found")


def tasks_run():
    orders = change_status_after_creation.delay()
    change_status_finally.delay(orders)  # type: ignore
