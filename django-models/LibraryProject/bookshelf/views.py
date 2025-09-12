from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    """A basic function view returning a greeting message."""
    return HttpResponse("Hello, World!")

# Create your views here.
