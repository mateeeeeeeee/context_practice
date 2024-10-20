from django.shortcuts import render

def ip_address_procesor(request):
    return {"ip_address": request.META['REMOTE_ADDR']}

def index(request):
    return render(request, 'index.html', ip_address_procesor(request))