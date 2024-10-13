# greetings/views.py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

def greet_name(request, name):
    capitalized_name = name.capitalize()
    return HttpResponse(f"Hello {capitalized_name}!")
