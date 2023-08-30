from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from ordersapp.models import Order
from ordersapp.views import OrdersCreateListViewSets, OrdersUpdateView, OrdersRetrieveViewSet



class OrderTests(APITestCase):

    _factory = APIRequestFactory()

    def test_get_order(self):
        """
        Ensure we can create an order
        """

        view = OrdersCreateListViewSets.as_view({'get': 'list'})
        request = self._factory.get('/orders/')
        
        response = view(request)
        response.render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_create_order(self):
        """
        Ensure we can create an order
        """

        view = OrdersCreateListViewSets.as_view({'post': 'create'})
        data = {
            "client": "Jack Sparrow",
            "arrival_from": "Caribean Sea: Port Tortuga",
            "destination_to": "Port Norfolk",
        }
        request = self._factory.post('/orders/', data)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().client, "Jack Sparrow")
        self.assertEqual(Order.objects.get().arrival_from, "Caribean Sea: Port Tortuga")
        self.assertLessEqual(len(Order.objects.get().arrival_from), 100)


    def test_update_order(self):
        """
        Ensure we can update orders
        """

        view = OrdersUpdateView.as_view()
        data = {
            "client": "Big Dick",
            "arrival_from": "Sex Shop",
            "destination_to": "Sad 45 years old broad",
        }
        request = self._factory.put('/orders/ce444f6f-d21a-45da-b26a-b0356f33385f', data, format='json')
        
        response = view(request)

        self.assertNotEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Order.objects.get().client, "Big Dick")
        self.assertEqual(Order.objects.get().arrival_from, "Sex Shop")
        self.assertEqual(Order.objects.get().destination_to, "Sad 45 years old broad")
        self.assertContains(Order.objects.get().status, "New")
        self.assertFieldOutput(Order.objects.get().length, '')
        self.assertFieldOutput(Order.objects.get().width, '')
        

    def test_retrieve_order(self):
        """
        Ensure we can update orders
        """
        view = OrdersRetrieveViewSet.as_view({'get': 'retrieve'})
        request = self._factory.get('/order/de4eda37-40ed-4c82-8fc8-ed9ec0edf4e0')
        response = view(request, pk='de4eda37-40ed-4c82-8fc8-ed9ec0edf4e0')
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertRaisesMessage(expected_exception=Order.DoesNotExist, expected_message="Order with parcel serial number not found")
        self.assertIsNotNone(Order.objects.get().status)
        self.assertEqual(response.content, Order.objects.get().status)
