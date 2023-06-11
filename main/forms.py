from django import forms

class Product2CartFrom(forms.Form):
    count = forms.IntegerField(min_value=1)
