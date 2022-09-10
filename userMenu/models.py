from django.db import models

# Create your models here.
class UserIntreface(models.Model):
    username = models.CharField(max_length=100)
    eaten = models.IntegerField()
    toEat = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    #picture = models.ImageField()
    userCreated = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class History(models.Model):
    caloriesEaten = models.IntegerField()
    caloriesToEat = models.IntegerField()
    date = models.DateField()

class Meals(models.Model):
    breakfast = models.IntegerField()
    lunch = models.IntegerField()
    dinner = models.IntegerField()

class MealList(models.Model):
    breakfast = models.CharField(max_length=400)
    lunch = models.CharField(max_length=400)
    dinner = models.CharField(max_length=400)