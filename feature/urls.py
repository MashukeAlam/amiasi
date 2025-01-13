from django.urls import path
from . import views

app_name = 'feature'

urlpatterns = [
    path('', views.create_feature, name='index'),
]
