from django.contrib import admin
from .models import *


admin.site.register([SeasonModels, PartModels])
@admin.register(MovieModels)
class JoyLinkUserAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category', 'is_active', 'key']
    ordering = ['-create_time']
    list_editable = ['is_active', 'category']
    search_fields = ['title']
    list_filter = ['is_active']