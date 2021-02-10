from django.shortcuts import render

# Create your views here.


def HomeView(request, *args, **kwargs):
	return render(request, 'products/index.html')


def CategoryView(request, *args, **kwargs):
	return render(request, 'products/category.html')

def BlogView(request, *args, **kwargs):
	return render(request, 'products/blog.html')

def ContactUsView(request, *args, **kwargs):
	return render(request, 'products/contact.html')


