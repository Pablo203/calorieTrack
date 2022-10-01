from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.menu, name='menu'),
    path('newDate/', views.newDate, name="date"),
    path('history/', views.history, name="history"),
    path('newProduct/', views.addNewProduct, name='newProduct'),
    path('newProductExecute/', views.newProductExecute, name="newProductExecute"),
    path('productsList/', views.productsList, name="productList"),
    path('product/<int:id>/', views.productDetail, name="productDetail"),
    path('<str:historyDate>/', views.historyDetail, name='historyDetail'),
    path('<str:meal>/', views.showProductsToAdd, name="showProd"),
    path('<str:meal>/<str:product_name>/', views.addProductToMeal, name='meal'),
]

urlpatterns = format_suffix_patterns(urlpatterns)