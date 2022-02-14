from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_form, name='client_form'), # client_form to get the form to add a new client
    path('<int:id>/', views.client_form, name='client_update'), # client_update to get the form to update a client
    path('delete/<int:id>/', views.client_delete, name='client_delete'), # client_delete to delete a client
    path('client_list/', views.client_list, name='client_list'), # client_list to get the list of clients
]
