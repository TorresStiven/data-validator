# validator/views.py

import csv
from django.shortcuts import render
# Importamos el formulario personalizado que valida el archivo (extensión, tamaño, etc.)
from .forms import CSVUploadForm
# Importamos una función que valida una fila individual del CSV (definida en validators.py)
from .validators import validate_row


def home(request):
    # Vista simple que renderiza la plantilla 'home.html' (normalmente muestra el formulario)
    return render(request, "home.html")


def upload_csv(request):
    # Inicializamos contenedores para:
    # - rows: filas que vamos guardando (actualmente se añaden todas)
    # - errors: lista de errores encontrados durante la validación de filas
    # - success: flag para indicar si el procesamiento fue exitoso
    rows = []
    errors = []
    success = False

    # Comprobamos si la petición es POST (es decir, si se envió el formulario)
    if request.method == "POST":
        # Creamos una instancia del formulario con los datos POST y los archivos subidos
        form = CSVUploadForm(request.POST, request.FILES)

        # Validamos el formulario (esto verifica la extensión, tamaño, etc. según lo definido en forms.py)
        if form.is_valid():
            # Obtenemos el archivo subido desde request.FILES
            csv_file = request.FILES["csv_file"]

            # Leemos todo el contenido del archivo, lo decodificamos a UTF-8 y lo separamos por líneas.
            # NOTA: esto carga el archivo entero en memoria; puede ser un problema con archivos grandes.
            decoded = csv_file.read().decode("utf-8").splitlines()

            # Creamos un lector CSV que itera sobre las líneas (separa en columnas según el CSV)
            reader = csv.reader(decoded)

            # Recorremos cada fila con su índice (empezando en 1)
            for index, row in enumerate(reader, start=1):
                # Validamos la fila con la función validate_row; debe devolver una lista de errores (vacía si OK)
                row_errors = validate_row(row, index)

                # Si hay errores para esta fila, los añadimos a la lista global de errores
                if row_errors:
                    errors.extend(row_errors)

                # Añadimos la fila a 'rows' (nota: actualmente se añade incluso si tiene errores)
                rows.append(row)

            # Si después de procesar todas las filas no hay errores, marcamos el procesamiento como exitoso
            if not errors:
                success = True

    else:
        # Si no es POST (p. ej. GET), creamos un formulario vacío para mostrarlo en la plantilla
        form = CSVUploadForm()

    # Finalmente renderizamos 'home.html' pasando:
    # - form: el formulario (vacío o con errores)
    # - rows: las filas leídas
    # - errors: lista de errores encontrados
    # - success: booleano que indica si todo fue correcto
    return render(request, "home.html", {
        "form": form,
        "rows": rows,
        "errors": errors,
        "success": success
    })