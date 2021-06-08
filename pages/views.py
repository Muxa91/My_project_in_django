from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'pages/first.html')

def product(request):
    return render(request, 'pages/product_pc.html')

def registration(request):
    return render(request, 'pages/registration.html')

def sing_up(request):
    return render(request, 'pages/sing-up.html')