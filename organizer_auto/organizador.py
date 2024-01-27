import os
import shutil

# Diccionario que mapea extensiones de archivo a nombres de carpeta, puedes agregar o repetir
extensiones_dict = {
    '.pdf': 'documentos_pdf',
    '.txt': 'documentos_word',
    '.docx': 'documentos_word',
    '.csv': 'tablas_DocExcel',
    '.jpg': 'imagenes',
    '.png': 'imagenes',
    '.mp3': 'sound',
    '.zip': 'comprimidos',
    '.rar': 'comprimidos',
    '.py': 'codigo_python',
    '.ipynb': 'codigo_python',
    '.java': 'codigo_java',
    '.mlx': 'codigo_MATLAB',
    '.m': 'codigo_MATLAB',
    '.rmd': 'codigo_R',
    '.exe': 'ejecutable',
}

# Nombre predeterminado de la carpeta para archivos no reconocidos (puedes cambiar el nombre a tu gusto)
pred = 'REVISAR'

# Ruta de la carpeta de descargas o añade la que quieras usar
carpeta = r'C:\Users\Downloads'

# Lista de TODOS los archivos en la carpeta de descargas
archivos = os.listdir(carpeta)

# Iterar sobre cada archivo en la carpeta de descargas
for archivo in archivos:
    archivo_origen = os.path.join(carpeta, archivo)
    
    # Si el archivo es un archivo (no una carpeta)
    if os.path.isfile(archivo_origen):
        _, extension = os.path.splitext(archivo)
        
        # Obtener el nombre de la carpeta correspondiente a la extensión del archivo
        nombre_carpeta = extensiones_dict.get(extension.lower(), pred)
        
        # Crear la ruta de destino de la carpeta
        archivo_destino = os.path.join(carpeta, nombre_carpeta)
        
        # Si la carpeta de destino no existe, crearla
        if not os.path.exists(archivo_destino):
            os.makedirs(archivo_destino)
            
        # Mover el archivo a la carpeta de destino
        shutil.move(archivo_origen, archivo_destino)
