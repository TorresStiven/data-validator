from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()

# CSVUploadForm es el contrato que le dice a Django
# Espero un archivo llamado csv_file,
# no continúes si no llega bien”.