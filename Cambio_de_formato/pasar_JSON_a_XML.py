# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 17:53:29 2024

@author: DiegoDePablo
"""
import json
import xml.etree.ElementTree as ET

def transformar_a_xml(documentos, root_name="root", item_name="item"):
    """
    Transforma una lista de documentos JSON a un formato XML.
    
    Args:
        documentos (list): Lista de diccionarios que representan el JSON.
        root_name (str): Nombre de la raíz en el XML.
        item_name (str): Nombre de los elementos hijos.
    
    Returns:
        str: Cadena XML generada.
    """
    def procesar_elemento(parent, key, value):
        """
        Procesa un elemento individual del JSON para agregarlo al XML.
        """
        if isinstance(value, dict):
            child = ET.SubElement(parent, key)
            for sub_key, sub_value in value.items():
                procesar_elemento(child, sub_key, sub_value)
        elif isinstance(value, list):
            list_parent = ET.SubElement(parent, key)
            for item in value:
                procesar_elemento(list_parent, "item", item)
        else:
            child = ET.SubElement(parent, key)
            child.text = str(value)

    root = ET.Element(root_name)
    for doc in documentos:
        item = ET.SubElement(root, item_name)
        for key, value in doc.items():
            procesar_elemento(item, key, value)
    return ET.tostring(root, encoding='utf-8').decode('utf-8')


if __name__ == "__main__":
    # Leer el archivo JSON
    try:
        with open("c3.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
        # Convertir el JSON a XML
        xml_output = transformar_a_xml(data, root_name="tratamientos", item_name="tratamiento")
        
        # Guardar el XML en un archivo
        with open("c3.xml", "w", encoding="utf-8") as xml_file:
            xml_file.write(xml_output)
        
        print("Archivo XML generado exitosamente como 'c3.xml'.")
    
    except Exception as e:
        print(f"Error al procesar: {e}")
