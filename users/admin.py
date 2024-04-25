from django.contrib import admin
from .models import Contact
from import_export.admin import ImportExportModelAdmin


@admin.register(Contact)
class ContactsAdmin(ImportExportModelAdmin):
    list_display = ('last_name', 'email', 'nomber', 'comment')
    search_fields = ('last_name', 'email', 'nomber', 'comment')
