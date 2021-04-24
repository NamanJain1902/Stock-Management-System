from django import forms

from .models import Stock

class StockCreateForm(forms.ModelForm):
  class Meta:
    model = Stock
    fields = ['category', 'item_name', 'quantity']
  
  def is_valid(self):
    return True