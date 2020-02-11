from django.urls import path
from orderapp.views import placeOrderView,showOrderView,confirmOrder
urlpatterns = [
	path('placeOrderView/',placeOrderView),
	path('showorder/',showOrderView),
    path('confirmOrder/',confirmOrder)
]

