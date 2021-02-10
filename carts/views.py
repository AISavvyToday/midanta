from django.shortcuts import render

# Create your views here.
def CartView(request, *args, **kwargs):
	return render(request, 'carts/cart.html')