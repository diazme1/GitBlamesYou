# Armamos el TXT de salida

def salida_txt(output_file, current_branch, lineas_por_archivo, lineas_global_por_autor):
    salida = []

    salida.append(f"📊Resumen de líneas por autor - 🌿Rama: {current_branch}\n")

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

    # Imprimir en consola
    print("\n".join(salida))

    # Guardar en archivo .txt
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(salida))