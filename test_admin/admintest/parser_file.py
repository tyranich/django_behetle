import tablib
from import_export import resources
from .models import MODELS_XLS

"""
file_resource = resources.modelresource_factory(model=MODELS_XLS)()
dataset = tablib.Dataset(["", "test"], header =["one", "two", "three", "four", "средняя цена"])
result = file_resource.import_data(dataset, dru_run=True)
"""