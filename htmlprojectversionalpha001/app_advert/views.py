from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(requests):
    return render(requests, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')