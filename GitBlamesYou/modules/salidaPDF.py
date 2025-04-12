from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

# ✍️ Generar PDF
def salida_pdf(output_pdf, current_branch, lineas_por_archivo, lineas_global_por_autor):
    pdf = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    x, y = 2 * cm, height - 2 * cm

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, f"Resumen de líneas por autor - Rama: {current_branch}")
    y -= 1.2 * cm

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(x, y, "Totales globales por autor:")
    y -= 0.8 * cm
    pdf.setFont("Helvetica", 10)

    for autor, total in sorted(lineas_global_por_autor.items(), key=lambda x: -x[1]):
        pdf.drawString(x + 0.5 * cm, y, f"{autor}: {total} líneas")
        y -= 0.4 * cm
    y -= 0.8 * cm
    pdf.setFont("Helvetica", 10)

    for archivo, autores in sorted(lineas_por_archivo.items()):
        archivo_name = archivo.split("/")[-1]
        if y < 2 * cm:
            pdf.showPage()
            y = height - 2 * cm
            pdf.setFont("Helvetica", 10)

        pdf.drawString(x, y, f"Archivo: {archivo_name}")
        y -= 0.5 * cm
        for autor, count in sorted(autores.items(), key=lambda x: -x[1]):
            pdf.drawString(x + 0.5 * cm, y, f"{autor}: {count} líneas")
            y -= 0.4 * cm
        y -= 0.4 * cm

    if y < 3 * cm:
        pdf.showPage()
        y = height - 2 * cm
        pdf.setFont("Helvetica", 10)


    pdf.save()