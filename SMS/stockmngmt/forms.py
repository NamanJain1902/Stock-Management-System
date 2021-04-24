from django import forms

from .models import Stock

class StockCreateForm(forms.ModelForm):
  """
  A metaclass in Python is a class of a class that defines 
  how a class behaves. A class is itself an instance of a metaclass.
  """
  class Meta:
    model = Stock
    fields = ['category', 'item_name', 'quantity']
  
  def is_valid(self):
    return True