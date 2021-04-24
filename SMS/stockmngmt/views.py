from django.shortcuts import render, redirect
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
  form = StockSearchForm(request.POST or None)
  title = "List of Items."
  querySet = Stock.objects.all()
  context = {
    "form": form,
    "title" : title,
    "querySet": querySet 
  }

  if request.method == 'POST':
    querySet = Stock.objects.filter(category__icontains=form['category'].value(),
                                    item_name__icontains=form['item_name'].value())
    context = {
      "form": form,
      "title" : title,
      "querySet": querySet 
    }

  return render(request, "list_items.html", context)

def add_items(request):
  form = StockCreateForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('/items')
  
  context = {
    "form": form,
    "title": "ADD ITEM",
  }

  return render(request, "add_items.html", context)