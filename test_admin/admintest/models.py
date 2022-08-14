from turtle import mode
from unicodedata import name
from django.db import models
import os
import openpyxl
# Create your models here.

class MODELS_XLS(models.Model):
    #name = models.CharField("test", max_length=100)
    one = models.CharField(name="one", max_length=15)
    two = models.CharField(db_column="two", max_length=15)
    three = models.CharField(db_column="three", max_length=15)
    four = models.CharField(db_column="four", max_length=15)
    midl_price = models.DecimalField(name="средняя цена", max_digits=10, decimal_places=2,db_index=False, null=True, blank=True)

    #def __str__(self):
        #return self.name


#class FILE_XLS(models.Model):
    #file = models.FileField(upload_to='static')

    #def filename(self):
        #return os.path.basename(self.file.name)


#file = FILE_XLS.objects.get(name)
#wb = openpyxl.load_workbook(file)