# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:55:03 2024

@author: DiegoDePab
"""
import os
from PIL import Image
import numpy as np

# Función para convertir archivos BMP a archivos .h
def bmp_to_header(bmp_file, output_file, array_name):
    img = Image.open(bmp_file)
    img = img.convert("RGB")  # Convertir a formato RGB
    img = img.resize((160, 128))  # Redimensionar la imagen a 160x128 (ajustado a la pantalla)

    # Obtener los datos de píxeles en formato hexadecimal
    pixel_data = np.array(img)
    hex_data = []

    for row in pixel_data:
        for pixel in row:
            # Extraer componentes de color y convertir a formato RGB565
            r = pixel[0] >> 3
            g = pixel[1] >> 2
            b = pixel[2] >> 3
            hex_val = (r << 11) | (g << 5) | b  # Convertir a formato de 16 bits
            hex_data.append(f"0x{hex_val:04X}")  # Formatear como hexadecimal

    # Guardar los datos en un archivo .h con un nombre de array único
    with open(output_file, 'w') as f:
        f.write(f"const unsigned short {array_name}[{len(hex_data)}] PROGMEM = {{\n")
        for i in range(0, len(hex_data), 16):
            f.write(", ".join(hex_data[i:i+16]) + ",\n")
        f.write("};\n")

# Carpeta de entrada (contiene los archivos BMP)
input_folder = "frames_pulsera/"
# Carpeta de salida (donde se guardarán los archivos .h)
output_folder = "output_headers/"
os.makedirs(output_folder, exist_ok=True)  # Crear la carpeta de salida si no existe

# Procesar todos los archivos BMP en la carpeta
for i, filename in enumerate(sorted(os.listdir(input_folder))):
    if filename.endswith(".bmp"):
        bmp_file = os.path.join(input_folder, filename)
        # Generar el nombre de salida con ceros a la izquierda para asegurar el orden
        output_file = os.path.join(output_folder, f"frame_{str(i).zfill(3)}.h")
        array_name = f"frame_{str(i).zfill(3)}"  # Nombre del array con ceros a la izquierda
        bmp_to_header(bmp_file, output_file, array_name)
        print(f"Generado: {output_file}")