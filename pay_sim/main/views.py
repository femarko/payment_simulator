from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from main.serializers import PaymentSerializer

from main.models import Payment



def index(request):
    return render(request, 'index.html')


def check_status(request) -> HttpResponse:
    id = request.GET.get('id')
    payment = Payment.objects.get(id=id)
    status = payment.status
    return render(request, 'check_status.html', {'status': status})


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer



