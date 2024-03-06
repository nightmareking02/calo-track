from django.contrib import admin
from calapp.models import calmodel,savemodel,finalmodel

# Register your models here.


admin.site.register(calmodel)
admin.site.register(savemodel)
admin.site.register(finalmodel)