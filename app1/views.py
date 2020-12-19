from django.shortcuts import render,redirect
from time import gmtime, strftime
# Create your views here.
def index(request):
    return render(request, "index.html")