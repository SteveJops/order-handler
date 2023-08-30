from .models import Order
from celery import shared_task
from celery.utils.log import get_task_logger
from typing import List, Tuple

logger = get_task_logger(__name__)
STATUSES: Tuple[str, str] = ("Given", "Refusal")  # type: ignore


@shared_task
def change_status_after_creation() -> List[Order,]:
    """
    Function for scheduled changing parcer`s status after 3 minutes after creation of order

    Returns:
        List[Order,]: list with orders where was changed status to "placed"
    """
    logger.info("Changing status to placed has been started")
    final_status_of_orders = list()
    orders = Order.objects.filter(status="New")
    for order in orders:
        order.status = "Placed"
        order.save()
        final_status_of_orders.append(order)
    return final_status_of_orders


@shared_task
def change_status_finally(final_status_of_orders: List[Order,]) -> None:
    """
    Function for scheduled changing parcer`s status the last status changing to final status

    Args:
        final_status_of_orders (List[Order,]): list with orders and firstly changed statuses
    """
    import random

    logger.info("Changing status to random one has been started")

    for order in final_status_of_orders:
        record: Order = Order.objects.get(pk=order)
        record.status = random.choice(STATUSES)
        record.save()


# if __name__ == "__main__":
#     orders = change_status_after_creation()
#     change_status_finally(orders)
