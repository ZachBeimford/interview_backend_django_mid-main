from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class DeactivateOrderView(APIView):
    def post(self, request, pk):
        deactivated_order = Order.objects.get(pk=pk)
        if deactivated_order.is_active:
            deactivated_order.deactivate()
        deactivated_order.save()
        return Response(status=202)