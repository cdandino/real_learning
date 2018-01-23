from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Textbook

def index(request):
    textbooks = Textbook.objects.all()
    return render(request, 'textbook/index.html', {"textbooks" : textbooks })

def contents(request, title):
    book = Textbook.objects.get(title=title)
    return render(request, 'textbook/contents.html', {"book" : book})



# Create your views here.
