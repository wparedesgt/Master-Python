from django.contrib import admin
from .models import Page

#Configuracion Extra

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)


# Register your models here.

admin.site.register(Page, PageAdmin)

title = "Proyecto William Paredes"
subtitle = "Panel de Gestion"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle