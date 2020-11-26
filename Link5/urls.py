from django.urls import path
from Link5 import views

urlpatterns = [
    path('', views.Link5, name='Link5'),
    path('viewInventory/', views.viewInventory, name='viewInventory'),
    path('addSales/', views.addSales, name='addSales'),
    path('updateInventory/', views.updateInventory, name='updateInventory'),
    path('deleteEntry/<eid>', views.deleteEntry, name='deleteEntry'),
]

