from django.contrib import admin
from .models import UserIntreface, MealList, Meals, Product, History

# Register your models here.
admin.site.register(UserIntreface)
admin.site.register(MealList)
admin.site.register(Meals)
admin.site.register(Product)
admin.site.register(History)