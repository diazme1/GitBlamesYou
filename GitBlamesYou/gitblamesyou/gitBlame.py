import argparse
import os
import subprocess
import re
from collections import defaultdict
from gitblamesyou.salidaTXT import salida_txt
from gitblamesyou.salidaPDF import salida_pdf

def main():
    repo_path = os.getcwd()
    EXTENSIONES_VALIDAS = ['.java']

    # Nos movemos al directorio del repo
    #os.chdir(repo_path)
    parser = argparse.ArgumentParser(description="Argumentos blaming")
    parser.add_argument('--branch', '-b', help='Rama a analizar', required=True)
    parser.add_argument('--outputTXT', '-oT', help='Nombre del archivo txt de salida')
    parser.add_argument('--outputPDF', '-oP', help='Nombre del archivo pdf de salida')

    args = parser.parse_args()

    current_branch = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']
    ).decode('utf-8').strip()

    if current_branch != args.branch:
        try:
            #En caso de querer controlar remoto, se debe hacer pull antes de ejecutar:
            subprocess.run(['git', 'checkout', args.branch])
        except subprocess.CalledProcessError as e:
            print(e)

    # Diccionarios para conteo
    lineas_global_por_autor = defaultdict(int)
    lineas_por_archivo = defaultdict(lambda: defaultdict(int))

    # Regex para extraer nombre hasta la fecha (captura "Juan Pérez" en el blame)
    regex_autor = re.compile(r'\((.+?)\s+\d{4}-\d{2}-\d{2}')  # Hasta el año

    for root, dirs, files in os.walk("."):
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

    #Salida por consola:
    salida = []
    salida.append(f"📊Resumen de líneas por autor - 🌿Rama: {args.branch}\n")

    salida.append("📊 Total global por autor:")
    for autor, total in sorted(lineas_global_por_autor.items(), key=lambda x: -x[1]):
        salida.append(f"{autor}: {total} líneas")
    salida.append("")

    salida.append("📁 Líneas por archivo y autor:\n")
    for archivo, autores in sorted(lineas_por_archivo.items()):
        archivo_name = archivo.split("/")[-1]
        salida.append(f"📝 {archivo_name}")
        for autor, count in sorted(autores.items(), key=lambda x: -x[1]):
            salida.append(f"   {autor}: {count} líneas")
        salida.append("")

    print("\n".join(salida))

    #Guardado de archivos:
    contributions_dir = os.path.join(repo_path, "contributions")
    if args.outputTXT:
        os.makedirs(contributions_dir, exist_ok=True)
        output_txt = os.path.join(contributions_dir, args.outputTXT + ".txt")
        salida_txt(output_txt, salida)
        print(f"\n✅ Resumen guardado en {output_txt}")

    if args.outputPDF:
        os.makedirs(contributions_dir, exist_ok=True)
        output_pdf = os.path.join(contributions_dir, args.outputPDF + ".pdf")
        salida_pdf(output_pdf, args.branch, lineas_por_archivo, lineas_global_por_autor)
        print(f"\n✅ Resumen guardado en {output_pdf}")

if __name__ == '__main__':
    main()