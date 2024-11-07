from django.contrib import admin

# Register your models here.
from .models import Topic, Recipe


admin.site.register(Recipe)
admin.site.register(Topic)