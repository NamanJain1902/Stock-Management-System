from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
  title = "Welcone: This is the home page."
  context = {
    "title" : title,
  }

  return render(request, "home.html", context)

def list_items(request):
  title = "List of Items."
  querySet = Stock.objects.all()
  context = {
    "title" : title,
    "querySet": querySet 
  }

  return render(request, "list_items.html", context)

def add_items(request):
  form = StockCreateForm(request.POST or None)
  # if form.is_valid():
  form.save()
  
  context = {
    "form": form,
    "title": "ADD ITEM",
  }

  return render(request, "add_items.html", context)