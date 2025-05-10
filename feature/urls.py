from django.urls import path
from . import views

app_name = 'feature'

urlpatterns = [
    path('', views.create_feature, name='index'),
    path('youtube-view/', views.youtube_view, name='youtube_view'),
    path('youtube-sub/', views.youtube_sub, name='youtube_sub'),
    path('youtube-like/', views.youtube_like, name='youtube_like'),
    path('consume-feature/', views.consume_feature, name='consume_feature'),
]
