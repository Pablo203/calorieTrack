from django.db import models
import datetime

# Create your models here.
class UserIntreface(models.Model):
    username = models.CharField(max_length=100)
    eaten = models.IntegerField(default=0)
    toEat = models.IntegerField(default=3500)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    #picture = models.ImageField()
    #userCreated = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class History(models.Model):
    caloriesEaten = models.IntegerField()
    caloriesToEat = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Meals(models.Model):
    breakfast = models.IntegerField(default=0)
    lunch = models.IntegerField(default=0)
    dinner = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.date)

class MealList(models.Model):
    breakfast = models.CharField(max_length=400)
    lunch = models.CharField(max_length=400)
    dinner = models.CharField(max_length=400)
    date = models.DateField(default=datetime.date.today())

    def __str__(self):
        return str(self.date)