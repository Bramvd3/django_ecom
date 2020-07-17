from django.shortcuts import render
from .models import Item
# Create your views here.


def item_list(request):
    context = {
        'item': Item.objects.all()
    }
    return render(request, "item_list.html", context)
