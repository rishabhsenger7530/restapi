from django.contrib import admin

from .models import TestModel
# Register your models here.

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['name','description','phone','is_alve', 'extra_name','amount','created_at','updated_at']