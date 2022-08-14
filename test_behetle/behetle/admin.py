from tkinter import Widget
from xml.etree.ElementTree import TreeBuilder
from django.contrib import admin
from .models import TABLE_FIELDS, FILE_MODEL, MODELS_XLS
from import_export.admin import ImportExportActionModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


# Register your models here.

@admin.register(MODELS_XLS)
class XLS_FILE(ImportExportModelAdmin):
    pass

#admin.site.register((XLS_FILE, TABLE_FIELDS))