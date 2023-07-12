from django.shortcuts import render


def home(request):
    return render(request, 'store/home.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')