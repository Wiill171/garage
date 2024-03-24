from django.urls import path
from .views import (
    post_detail,
    post_list,
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
    VeiculoListView,
    VeiculoDetailView,
    VeiculoCreateView,
    VeiculoDeleteView,
    VeiculoUpdateView
    )

app_name = 'garage'

urlpatterns = [
    
    path('', post_list, name='post_list'),
    path('<int:id>/', post_detail, name='post_detail'),

    path('clientes', ClienteListView.as_view(), name='client-view'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='client-detail'),
    path('clientes/new/', ClienteCreateView.as_view(), name='client-create'),
    path('clientes/<int:pk>/update/', ClienteUpdateView.as_view(), name='client-update'),
    path('clientes/<int:pk>/delete/', ClienteDeleteView.as_view(), name='client-delete'),
    
    path('veiculos', VeiculoListView.as_view(), name='veiculo-view'),
    path('veiculos/<int:pk>/', VeiculoDetailView.as_view(), name='veiculo-detail'),
    path('veiculos/new/', VeiculoCreateView.as_view(), name='veiculo-create'),
    path('veiculos/<int:pk>/update/', VeiculoUpdateView.as_view(), name='veiculo-update'),
    path('veiculos/<int:pk>/delete/', VeiculoDeleteView.as_view(), name='veiculo-delete'),
    
]