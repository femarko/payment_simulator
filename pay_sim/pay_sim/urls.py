"""
URL configuration for pay_sim project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import (
    path,
    include,
)

from main.views import (
    index,
    check_status,
    PaymentViewSet,
)

router = DefaultRouter()
router.register('', PaymentViewSet, basename='api')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment-simulator/', index, name='index'),
    path('payment-simulator/', check_status, name='check_status'),
    path('payment-simulator/api/', include(router.urls)),
]
