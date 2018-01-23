from django.contrib import admin

from .models import *

admin.site.register(Textbook)
admin.site.register(Chapter)
admin.site.register(Section)

# Register your models here.
