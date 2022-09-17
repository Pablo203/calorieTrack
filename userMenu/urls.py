from django.urls import path, register_converter
from . import converters
from . import views

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', views.menu, name='menu'),
    path('newDate/', views.newDate, name="date"),
    path('history/', views.history, name="history"),
    path('<str:meal>/', views.showProductsToAdd, name="showProd"),
    path('<str:meal>/<str:product_name>/', views.addProductToMeal, name='meal')
]