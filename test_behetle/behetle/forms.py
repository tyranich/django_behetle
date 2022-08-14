from distutils.command.upload import upload
from django import forms
 
class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    file = forms.FileField()
    #multi_form = forms.MultiValueField(fields=[, field2,..])