# views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World! It's a small small world")
