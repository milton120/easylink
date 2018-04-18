from django.contrib import admin

from .models import Tag, Category, Link


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'updated_at', 'updated_by', 'status')

    list_filter = ('status',)
    search_fields = ('name', 'alias')
    date_hierarchy = 'updated_at'

admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id', 'priority', 'updated_at', 'updated_by', 'status')

    list_filter = ('status',)
    search_fields = ('name', 'alias')
    date_hierarchy = 'updated_at'

admin.site.register(Category, CategoryAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'priority', 'category', 'updated_at', 'updated_by', 'status')

    list_filter = ('status',)
    search_fields = ('url', 'name', 'alias', 'category__name')
    date_hierarchy = 'updated_at'

admin.site.register(Link, LinkAdmin)