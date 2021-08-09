from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from bills.models import Bill
from bills.serializers import BillSerializer, CreateBillSerializer


class BillGenericView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
