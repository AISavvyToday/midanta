from django.shortcuts import render

# Create your views here.
def TrackOrderView(request, *args, **kwargs):
	return render(request, 'orders/tracking.html')