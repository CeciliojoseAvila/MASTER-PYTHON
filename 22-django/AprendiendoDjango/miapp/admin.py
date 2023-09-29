from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')  

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar el titulo del panel
title = "Máster en python - Cecilio Avila"
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de gestión"


"""class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)    
    list_display = ('name', 'created_at') 
    search_fields = ('name', 'description') """


"""class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name') 
    list_display = ('title', 'user', 'public', 'created_at')  
    list_filter = ('public', 'user__username', 'categories__name')"""

