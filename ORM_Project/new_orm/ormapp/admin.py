from django.contrib import admin
from .models import OrmModel
# Register your models here.
class OrmAdmin(admin.ModelAdmin):
    List_display = ['id', 'name', 'city', 'sal']

admin.site.register(OrmModel, OrmAdmin)
