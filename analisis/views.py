from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd

def home(request):
    return render(request, 'index.html', {'view': 'home'})

def subir_archivo(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        archivo = request.FILES['csv_file']
        fs = FileSystemStorage()
        filename = fs.save(archivo.name, archivo)
        file_url = fs.url(filename)

        df = pd.read_csv(fs.url(filename)[1:])
        resumen = df.describe()

        return render(request, 'index.html', {'view': 'view', 'resumen': resumen.to_html()})
    return render(request, 'index.html', {'view': 'upload'})
