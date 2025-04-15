<img src="https://www.meme-arsenal.com/memes/45f8e7ecbfff61861df9469f13fef765.jpg" alt="Git Blames You" width="325"/>

# 🕵️‍♂️ GitBlamesYou

**GitBlamesYou** es una herramienta diseñada para calcular los aportes realizados por distintos autores en cualquier repositorio Git.  
Analiza las firmas registradas en cada línea de código usando el comando `blaming`. Ideal para saber *quién escribió qué* 🔍.

---
## 🔄 Funcionamiento

**GitBlamesYou** ejecutará el comando `git blame`, y extraerá el autor de cada línea, en cada archivo presente, contabilizando dichos datos. Es decir, a diferencia de la contabilización de líneas realizada por **GitHub Insights**, no es un cálculo de líneas acumuladas agregadas en cada commit realizado. En su lugar, se calcularán el total de líneas actuales al momento de la ejecución del comando `blaming`.

---

## ⚙️ Instalación

1. 📥 Descarga el archivo: [🔗`gitblamesyou-0.1.tar.gz`](https://drive.google.com/uc?export=download&id=14hcMLveP9t8sQebHR84i2q6eNsmgGEnU
).
2. 💻 Ejecuta el siguiente comando:

```bash
pip install ruta_al_archivo/gitblamesyou-0.1.tar.gz
```

> ⚠️ **Importante**: Asegurate de que Python esté agregado a la variable `PATH` de tu sistema para que el comando `blaming` funcione correctamente.

---

## 🧰 Usos

GitBlamesYou permite:

- 📊 Calcular líneas aportadas por autor (global y por archivo).
- 📝 Guardar resultados en `.txt`.
- 📄 Exportar reportes en `.pdf`.

---

### 📌 Comando básico

```bash
blaming -b rama -e extensiones_deseadas
```

🔸 **Ejemplo:**

```bash
blaming -b main -e .java .py
```

> Evalúa los archivos de la rama `main` con extensiones `.java` y `.py`.

---

### 📝 Guardar como `.txt`

```bash
blaming -b rama -e extensiones_deseadas -oT archivo_output
```

🔸 **Ejemplo:**

```bash
blaming -b main -e .java .py -oT blaming_main
```

> Guarda el resultado en `contributions/blaming_main.txt`.

---

### 📄 Guardar como `.pdf`

```bash
blaming -b rama -e extensiones_deseadas -oP archivo_output
```

🔸 **Ejemplo:**

```bash
blaming -b main -e .java .py -oP blaming_main
```

> Guarda el resultado en `contributions/blaming_main.pdf`.

---

## 🧠 Nota importante

🔎 El cálculo se realiza **sobre la versión local** de los archivos.  
Si hay commits en plataformas remotas (como GitHub o GitLab) que aún no están en tu local, los resultados pueden no coincidir.

✔️ Para sincronizar tu copia local, simplemente se debe ejecutar:

```bash
git pull
```
