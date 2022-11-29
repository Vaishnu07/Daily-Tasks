from django.contrib import admin
from .models import category 
from .models import food


# Register your models here.
admin.site.register(category)
admin.site.register(food)