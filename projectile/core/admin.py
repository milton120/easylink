from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','email', 'country',
                    'gender', 'created_at', 'status')

    list_filter = ('status', 'gender')
    search_fields = ('first_name', 'last_name', 'email', 'alias', 'username')
    date_hierarchy = 'created_at'

admin.site.register(Person, PersonAdmin)
