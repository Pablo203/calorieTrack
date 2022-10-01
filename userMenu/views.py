from xmlrpc.client import ResponseError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import is_valid_path
from .models import UserIntreface, MealList, Meals, History, Product
from .forms import ProductForm
import datetime
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def menu(request):
    #meals = get_object_or_404(Meals,)
    meals = Meals.objects.last()
    if(meals.date != datetime.date.today()):
        newDate(request)
    user = get_object_or_404(UserIntreface, username="pablo")
    totalEaten = meals.breakfast + meals.lunch + meals.dinner
    caloriesToSubstract = totalEaten - user.eaten
    user.eaten = totalEaten
    if user.toEat - caloriesToSubstract < 0:
        user.toEat = 0
    else:
        user.toEat = user.toEat - caloriesToSubstract
    user.save()

    return render(request, 'index.html', {'user': user, 'mealList': MealList, 'meals': meals})

def newDate(request):
    user = get_object_or_404(UserIntreface, username="pablo")
    checkHistory = History.objects.all()

    if checkHistory == None:
        return HttpResponse("NONE")

    date = datetime.date.today() - datetime.timedelta(days=1)
    history = History.objects.create(caloriesEaten=user.eaten, caloriesToEat=user.toEat, date = date)
    meal = Meals.objects.create()
    mealList = MealList.objects.create(breakfast='', lunch='', dinner='')

    user.eaten = 0
    user.toEat = 3500

    history.save()
    meal.save()
    mealList.save()
    user.save()

    return HttpResponseRedirect('/calorie/')

def showProductsToAdd(request, meal):

    return render(request, 'addProduct.html', {'products': Product.objects.all(), 'meal': meal})   

def addProductToMeal(request, meal, product_name):
    requestedProd = get_object_or_404(Product, name=product_name)
    mealToAdd = get_object_or_404(Meals, date=datetime.date.today())

    if meal == "breakfast":
        mealToAdd.breakfast = mealToAdd.breakfast + requestedProd.calories
    elif meal == "lunch":
        mealToAdd.lunch = mealToAdd.lunch + requestedProd.calories
    elif meal == "dinner":
        mealToAdd.dinner = mealToAdd.dinner + requestedProd.calories

    mealToAdd.save()

    return HttpResponseRedirect('/calorie/')


def history(request):
    return render(request, 'history.html', {'history':History.objects.all()})

def historyDetail(request, historyDate):
    wantedDate = datetime.datetime.strptime(historyDate, '%Y-%m-%d')
    meals = get_object_or_404(Meals, date=wantedDate)
    return render(request, 'historyDetail.html', {'date': historyDate, 'meal': meals})

def addNewProduct(request):
    return render(request, 'addNewProduct.html')

def newProductExecute(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            newProduct = Product.objects.create(name=form.cleaned_data['name'], calories=form.cleaned_data['calories'])
            newProduct.save()
    return HttpResponseRedirect("/calorie")


@api_view(['GET', 'POST'])
def productsList(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return JsonResponse({"drinks" :serializer.data})

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)