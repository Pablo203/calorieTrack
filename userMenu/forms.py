from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label="name", max_length=100)
    calories = forms.IntegerField(label="calories")