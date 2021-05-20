from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail')
]
