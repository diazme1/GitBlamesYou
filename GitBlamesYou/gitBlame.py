import os
import subprocess
import re
from collections import defaultdict
from GitBlamesYou.modules.salidaTXT import salida_txt

#
# Agregar rama parametrizada y ejecutar comandos usando os para checkout y pull
# Definir entrypoints con parsenargs para opcionales de rutas de output files
# podría no parametrizarse la ruta, sino la posibilidad de output por consola o file
# en una carpeta de contributions por defecto
# y ruta de repo parametrizada o ruta actual.
#

repo_path = r"/Users/emiliadiaz/IdeaProjects/IntelliJentes"
GIT_PATH = r"C:\Program Files\Git\bin\git.exe"
EXTENSIONES_VALIDAS = ['.java']
output_txt = r"/Users/emiliadiaz/Documents/GitBlamesYou/Output/resumen_blame.txt"
#output_pdf = r"C:\Users\User\PycharmProjects\GitBlame\resumen_blame.pdf"

# Nos movemos al directorio del repo
os.chdir(repo_path)

try:
    current_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
    ).decode('utf-8').strip()
except subprocess.CalledProcessError:
    current_branch = "Desconocida"

# Diccionarios para conteo
lineas_global_por_autor = defaultdict(int)
lineas_por_archivo = defaultdict(lambda: defaultdict(int))

# Regex para extraer nombre hasta la fecha (captura "Juan Pérez" en el blame)
regex_autor = re.compile(r'\((.+?)\s+\d{4}-\d{2}-\d{2}')  # Hasta el año

for root, dirs, files in os.walk(".."):
    for file in files:
        if not any(file.endswith(ext) for ext in EXTENSIONES_VALIDAS):
            continue

        filepath = os.path.join(root, file).replace("\\", "/")

        try:
            output = subprocess.check_output(
                ['git', 'blame', filepath],
                stderr=subprocess.STDOUT
            )
            try:
                lines = output.decode('utf-8').splitlines()
            except UnicodeDecodeError:
                lines = output.decode('latin-1').splitlines()

            for line in lines:
                match = regex_autor.search(line)
                if match:
                    autor = match.group(1).strip()
                    lineas_global_por_autor[autor] += 1
                    lineas_por_archivo[filepath][autor] += 1
                else:
                    print(f"⚠️ No se pudo extraer autor en: {filepath}: {line}")

        except subprocess.CalledProcessError as e:
            print(f"❌ Error procesando {filepath}")
            try:
                print(e.output.decode('utf-8'))
            except UnicodeDecodeError:
                print(e.output.decode('latin-1'))


salida_txt(output_txt, current_branch, lineas_por_archivo, lineas_global_por_autor)
print(f"\n✅ Resumen guardado en {output_txt}")
# salida_pdf(output_pdf, current_branch, lineas_por_archivo, lineas_global_por_autor)
# print(f"\n✅ Resumen guardado en {output_pdf}")
