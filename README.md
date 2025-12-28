# Data Validator

## 📌 Descripción

**Data Validator** es una aplicación web desarrollada con **Django** que permite subir archivos CSV y validar su contenido de acuerdo con reglas estructurales y de negocio previamente definidas. La aplicación procesa el archivo en el backend, valida cada fila de manera independiente y muestra errores detallados indicando exactamente la fila y la columna donde ocurre cada fallo.

Este proyecto fue desarrollado como parte de una **prueba técnica**, con el objetivo de demostrar habilidades en desarrollo backend utilizando **Python** y **Django**, manejo de archivos, validaciones personalizadas y una estructura de proyecto clara y mantenible.

---

## 🚀 Funcionalidades

- Subida de archivos CSV desde una interfaz web
- Validación en backend utilizando Django Forms
- Validación fila por fila y por columna
- Reporte claro y detallado de errores
- Soporte para archivos con filas válidas e inválidas mezcladas
- Frontend simple enfocado en la funcionalidad

---

## 📂 Estructura del Proyecto

```
data-validator/
├── data_validator_app/
│   ├── forms.py          # Formularios Django para subida de archivos
│   ├── validators.py     # Lógica de validación del negocio
│   ├── views.py          # Manejo de peticiones
│   ├── urls.py           # Rutas de la aplicación
│   ├── templates/
│   │   └── home.html
│   └── static/
│       ├── css/
│       └── js/
├── examples/             # Archivos CSV de ejemplo
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🧪 Reglas de Validación

Cada archivo CSV debe cumplir con las siguientes reglas:

1. El archivo debe contener **exactamente 5 columnas** por fila
2. **Columna 1**: Número entero con una longitud entre **3 y 10 caracteres**
3. **Columna 2**: Correo electrónico con formato válido
4. **Columna 3**: Solo se permiten los valores `CC` o `TI`
5. **Columna 4**: Número entero entre **500000 y 1500000**
6. **Columna 5**: Texto libre (no se aplica validación)

Si una fila no cumple alguna regla, el sistema reporta el error indicando la **fila y la columna** correspondiente.

---

## 📁 Ejemplos

La carpeta `examples/` contiene archivos CSV de prueba para facilitar la validación del sistema:

- `example_valid.csv` → Archivo completamente válido
- `example_invalid.csv` → Archivo con errores consistentes
- `example_mixed_errors.csv` → Archivo con errores aleatorios en distintas filas y columnas

Estos archivos permiten demostrar el correcto funcionamiento de la lógica de validación.

---

## ⚙️ Cómo Ejecutar el Proyecto Localmente

1. Clonar el repositorio:

```bash
git clone https://github.com/TorresStiven/data-validator.git
cd data-validator
```

2. Crear y activar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

5. Abrir en el navegador:

```
http://127.0.0.1:8000/
```

---

## 🧠 Notas

- El frontend se mantiene intencionalmente simple, priorizando la lógica de backend
- Como mejora futura se podrían agregar pruebas automáticas, una vista previa del CSV y mejoras visuales

---

## 👤 Autor

**Stiven Torres**

---

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos y de evaluación técnica.
