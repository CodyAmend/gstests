from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
   path('client/register/', views.client_form, name='client_form'),
   path('client_list', views.client_list, name='client_list'),
   path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
   path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),
]