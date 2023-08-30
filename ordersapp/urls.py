from django.urls import include, path
from rest_framework import routers
from .views import OrdersCreateListViewSets, OrdersRetrieveViewSet, OrdersUpdateView


router = routers.DefaultRouter()
router.register(r"orders", OrdersCreateListViewSets)

urlpatterns = [
    path("ordersapp/", include(router.urls)),
    path("ordersapp/orders/<str:pk>", OrdersUpdateView.as_view()),
    path(
        "ordersapp/order/<str:pk>", OrdersRetrieveViewSet.as_view({"get": "retrieve"})
    ),
]
