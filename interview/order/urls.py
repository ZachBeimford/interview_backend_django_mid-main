
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrdersBetweenStartDateEmbargoDateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('preembargo/startdate/<int:start_year>/<int:start_month>/<int:start_day>/embargodate/<int:embargo_year>/<int'
         ':embargo_month>/<int:embargo_day>/', OrdersBetweenStartDateEmbargoDateView.as_view(), name='pre-embargo-list')
]