from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_node, name='create_node'),
    path('', views.node_list, name='node_list'),
]


