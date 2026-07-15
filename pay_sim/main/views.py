import random
import time
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from main.models import Payment



def index(request) -> HttpResponse:
    return render(request, 'index.html')


@api_view(['GET'])
def check_status(request, payment_id) -> Response:
    payment = get_object_or_404(Payment, id=payment_id)
    data = {"status": payment.status}
    time.sleep(random.randint(1, 5))
    return Response(data)
