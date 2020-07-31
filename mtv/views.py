from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request): 
    Mtv = mtv.objects.all()
    context = {
        'mtv': Mtv
    }
    return render(request, 'mtv/index.html', context)