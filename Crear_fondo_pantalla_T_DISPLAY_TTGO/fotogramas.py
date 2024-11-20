# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:53:19 2024

@author: DiegoDePablo
"""

from PIL import Image
import os

# Carga el GIF
gif_path = "gif.gif"
output_folder = "frames/"
os.makedirs(output_folder, exist_ok=True)

# Abre el GIF
im = Image.open(gif_path)

# Guarda cada fotograma como una imagen
for frame in range(0, im.n_frames):
    im.seek(frame)
    im.save(f"{output_folder}frame_0{frame}.bmp")
