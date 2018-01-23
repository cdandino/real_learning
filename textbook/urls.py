from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contents/<title>', views.contents, name='contents')
]
