from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('newDate/', views.newDate, name="date"),
    path('history/', views.history, name="history"),
    path('newProduct/', views.addNewProduct, name='newProduct'),
    path('newProductExecute/', views.newProductExecute, name="newProductExecute"),
    path('productsList/', views.productsList, name="productList"),
    path('<str:historyDate>/', views.historyDetail, name='historyDetail'),
    path('<str:meal>/', views.showProductsToAdd, name="showProd"),
    path('<str:meal>/<str:product_name>/', views.addProductToMeal, name='meal'),
    
]