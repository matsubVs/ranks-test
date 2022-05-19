from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('config/', views.stripe_config),
    path('buy/<int:item_id>/', views.buy),
    path('item/<int:item_id>/', views.ItemListView.as_view(), name='item'),
    path('order_buy/<int:order_id>/', views.buy_order),
    path('order/<int:order_id>/', views.OrderListView.as_view(), name='order'),
    path('success/', views.SuccessPageView.as_view()),
    path('cancel/', views.CancelPageView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()