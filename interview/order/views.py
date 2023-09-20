from rest_framework import generics
from rest_framework.response import Response
from datetime import datetime

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrdersBetweenStartDateEmbargoDateView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        start_date = datetime(self.kwargs["start_year"], self.kwargs["start_month"], self.kwargs["start_day"])
        embargo_date = datetime(self.kwargs["embargo_year"], self.kwargs["embargo_month"], self.kwargs["embargo_day"])
        serializer = self.serializer_class(self.queryset.filter(start_date=start_date).filter(embargo_date=embargo_date))

        return Response(serializer.data, status=200)
