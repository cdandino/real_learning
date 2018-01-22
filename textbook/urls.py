from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('content/<title>', views.content, name='content')
]
