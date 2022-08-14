from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import UserForm
#from .models import Person
"""
def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
"""
"""
def products(request, productid = 3):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)
 
def users(request, id=1, name='bob'):
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)
""" 

"""
def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Product № {0}  Category: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Tom")
    output = "<h2>User</h2><h3>id: {0}  name: {1}</h3>".format(id, name)
    return HttpResponse(output)
"""
"""
def index(request):
    return HttpResponse("Index")
 
def about(request):
    return HttpResponse("About")
 
def contact(request):
    return HttpResponseRedirect("/about")
 
def details(request):
    return HttpResponsePermanentRedirect("/")
"""

#def index(request):
    #a = "Hello Django"
    #b = "ololol"
    #data = {'header': a, "message": b}
    #return render(request, "behetle/index.html")
"""
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0} {1}</h2>".format(name, age))
    else:
        userform = UserForm()
        return render(request, "behetle/index.html", {"form": userform})
"""

"""
def index(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "behetle/index.html", {"form": userform})
"""
"""
def index(request):
    people = Person.objects.all()
    return render(request, "behetle/index.html", {"people": people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.name = request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
    return HttpResponseRedirect("/")

# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
 
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "behetle/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
     
# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

"""
"""
def downloads_file(request):
    excel_file = request.FILES["excel_file"]
    return HttpResponse("<h2>File download</h2>")
"""
from django.shortcuts import render
import openpyxl


def index(request):
    if "GET" == request.method:
        return render(request, 'behetle/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Лист1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'behetle/index.html', {"excel_data":excel_data})