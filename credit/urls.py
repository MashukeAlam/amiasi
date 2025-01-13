from django.urls import path
from .views import credit_request_view

urlpatterns = [
    path('request/', credit_request_view, name='credit_request'),
]
