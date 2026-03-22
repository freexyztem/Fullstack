"""Encuentra o crea algunos textos que te gustaría analizar (puedes visitar
Project Gutenberg (http://gutenberg.org/) o crear textos usando ChatGPT).
Copia el texto sin formato desde tu navegador en un archivo de texto en tu
computadora (o descarga los archivos). Averigua cuántas veces aparece una
palabra o frase en el texto (puedes usar el método count())."""

palabra = "de"
file_name = "texto.txt"
try:
    with open(file_name) as f:
        texto = f.read()
except:
    pass
else:
    print(f"la palabra '{palabra}' aparece ", texto.count(palabra), "veces")
