/* home_script.js
   Comportamiento para el formulario de subida CSV en `home.html`.
   - Muestra el nombre del archivo seleccionado
   - Valida extensión .csv (cliente)
   - Habilita / deshabilita botón de validar
   - Evita envío si no hay archivo válido
*/

document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('csvFile');
  const status = document.getElementById('fileStatus');
  const btn = document.getElementById('validateBtn');
  const form = document.getElementById('uploadForm');


  const setInvalid = (msg) => {
    status.textContent = msg;
    status.classList.remove('valid');
    status.classList.add('invalid');
    btn.disabled = true;
  };

  const setValid = (name) => {
    status.textContent = `Seleccionado: ${name}`;
    status.classList.remove('invalid');
    status.classList.add('valid');
    btn.disabled = false;
  };

  // Al cambiar la selección de archivo
  input.addEventListener('change', () => {
    const file = input.files[0];

    if (!file) {
      setInvalid('No se ha seleccionado archivo');
      return;
    }

    const name = file.name || '';
    const isCsvExt = name.toLowerCase().endsWith('.csv');

    // file.type puede no estar presente en algunos navegadores; nos apoyamos en extensión
    if (isCsvExt) {
      setValid(name);
    } else {
      setInvalid('Solo se permiten archivos con extensión .csv');
      input.value = ''; // limpiar selección inválida
    }
  });

  // Antes de enviar, verificamos que haya un archivo válido
  form.addEventListener('submit', (e) => {
    const file = input.files[0];
    if (!file || !file.name.toLowerCase().endsWith('.csv')) {
      e.preventDefault();
      setInvalid('Selecciona un archivo .csv válido antes de enviar');
      input.focus();
      return;
    }

    // Opcional: prevenir envíos duplicados
    btn.disabled = true;
    btn.textContent = 'Enviando...';
  });
});
