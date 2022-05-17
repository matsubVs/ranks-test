from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('buy/<int:item_id>', views.buy),
    path('item/<int:item_id>', views.item),
    path('success/', views.SuccessPageView.as_view()),
    path('cancelled/', views.CancelPageView.as_view()),
]