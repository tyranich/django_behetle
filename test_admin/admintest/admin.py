from django.contrib import admin
from .models import MODELS_XLS
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields


# Register your models here.
#@admin.register(MODELS_XLS)
#class XLS_FILE(ImportExportModelAdmin):
    #pass

class FileResource(resources.ModelResource):
    class Meta:
        model = MODELS_XLS
        #exclude = ('id', )
        import_id_fields = ("one", "two", "three", "four", "средняя цена")

class BookAdmin(ImportExportModelAdmin):
    resource_class = FileResource

admin.site.register(MODELS_XLS, BookAdmin)