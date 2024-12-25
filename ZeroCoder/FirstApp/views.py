from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'caption': 'Django'
    }
    return render(request, 'FirstApp/index.html', data)

def new(request):
    return render(request, 'FirstApp/new.html', {'caption': 'Django'})

