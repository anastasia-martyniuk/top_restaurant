from django.contrib import admin
from django.contrib.auth.models import Group

from pos_terminal.models import Printer, Check

# admin.site.register(Printer)
# admin.site.register(Check)


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ("printer", "type", "order", "status", "pdf_file")
    list_filter = ("printer", "type", "status")


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ("api_key", "name", "check_type", "check_type", "point_id")


admin.site.unregister(Group)
