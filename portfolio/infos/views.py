from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def me(request):
    return render(request, 'me.html')

def contact(request):
    return render(request, 'contact.html')
