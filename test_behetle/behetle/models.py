from locale import currency
from unicodedata import category
from django.db import models
import import_export


class FILE_MODEL(models.Model):
    """
    one = models.CharField("1", max_length=15)
    two = models.CharField("2", max_length=15)
    three = models.CharField("3", max_length=15)
    four = models.CharField("4", max_length=15)
    """
    XLS_FILE = models.FileField()
    date = models.CharField("Реальная дата", max_length=15)
    currency = models.CharField("Оригинальная валюта", max_length=40)
    closing_station = models.CharField("Станция закрытия", max_length=40)
    dish = models.CharField("Блюдо", max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    midl_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sum = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sum_pay = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 
    sell = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) 

class MODELS_XLS(models.Model):
    one = models.CharField(db_column="one", max_length=15)
    two = models.CharField(db_column="tw", max_length=15)
    three = models.CharField("3", max_length=15)
    four = models.CharField("4", max_length=15)

    

class TABLE_FIELDS(models.Model):
    date = models.DateField()          
    age = models.IntegerField()


