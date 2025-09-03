from django.urls import path
from . import views

urlpatterns = [
    path('', views.core_list, name='core_list'),
    path('create/', views.core_create, name='core_create'),
    path('edit/<int:core_id>/', views.core_edit, name='core_edit'),
    path('delete/<int:core_id>/', views.core_delete, name='core_delete'),
]

