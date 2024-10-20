from django.shortcuts import render

def ip_address_procesor(request):
    return {"ip_address": request.META['REMOTE_ADDR']}

def index(request):
    return render(request, 'index.html', ip_address_procesor(request))

def user(request):
    context = {
        'name': 'mate',
        'lastname': 'pkhakadze',
        'age': '14'
    }
    return render(request, 'user.html', context=context)