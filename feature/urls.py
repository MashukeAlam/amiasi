from django.urls import path
from . import views

app_name = 'feature'

urlpatterns = [
    path('', views.create_feature, name='index'),
    path('youtube-view/', views.youtube_view, name='youtube_view'),
    path('consume-feature/', views.consume_feature, name='consume_feature'),
]
