from django.urls import path
from . import views

urlpatterns = [
    path('items', views.ItemListView.as_view(), name='items_list'),
    path('items/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('buy/<int:pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', views.SuccessView.as_view(), name='success'),  
    path('cancelled/', views.CancelledView.as_view(), name='cancelled'),  
]
