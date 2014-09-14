from django.shortcuts import render
from .models import Order

# Create your views here.

def order_list(request):
    orders = Order.objects.order_by('date')
    return render(request, 'customers/order_list.html', {'orders': orders})
