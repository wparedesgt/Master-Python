from django.contrib import admin
from .models import Article, Category

# Register your models here.

#class ArticleAdmin(admin.ModelAdmin):
#    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Article)
admin.site.register(Category)
