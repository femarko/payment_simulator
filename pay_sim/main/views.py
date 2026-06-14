import random
import time
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from main.models import Payment



def index(request):
    return render(request, 'index.html')


@api_view(['GET'])
def check_status(request, payment_id) -> Response:
    payment = Payment.objects.get(id=payment_id)
    data = {"status": payment.status}
    time.sleep(random.randint(1, 5))
    return Response(data)



