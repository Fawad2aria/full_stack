from django.shortcuts import render, reverse, get_object_or_404
from .models import GroceryItem
from django.http import HttpResponseRedirect
from django.utils import timezone

def index(request):
    items = GroceryItem.objects.all()
    context = {
        'items': items
    }

    return render(request, 'grocery_list/index.html', context)


def add_more(request):
    description = request.POST['description']
    quantity = request.POST['quantity']
    unit = request.POST['unit']
    item= GroceryItem(description=description, quantity=quantity, unit=unit, created_date=timezone.now())
    item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def complete_todo(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.completed_date=timezone.now()
    item.completed = True
    item.save()

    return HttpResponseRedirect(reverse('grocery_list:index'))


def delete_item(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)    
    item.delete()

    return HttpResponseRedirect(reverse('grocery_list:index'))