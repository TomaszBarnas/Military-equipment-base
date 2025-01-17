from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),  # URL dla listy zasobów
    path('create/', views.resource_create, name='resource_create'),  # URL dla tworzenia nowego zasobu
    path('update/<int:pk>/', views.resource_update, name='resource_update'),  # URL dla edycji zasobu
    path('delete/<int:pk>/', views.resource_delete, name='resource_delete'),  # URL dla usuwania zasobu
]
