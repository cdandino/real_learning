from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Textbook

def index(request):
    textbooks = Textbook.objects.all()
    return render(request, 'textbook/index.html',{"textbooks" : textbooks })

# Create your views here.
