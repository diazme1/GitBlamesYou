# Armamos el TXT de salida

def salida_txt(output_file, salida):
    # Guardar en archivo .txt
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(salida))