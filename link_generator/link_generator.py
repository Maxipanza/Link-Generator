import os
import pathlib
from pathlib import Path

def obtener_path_del_escritorio():
    return os.path.join(os.path.join(os.environ['USERPROFILE'], 'Escritorio'))

def obtener_directorio_actual():
    return os.path.dirname(os.path.abspath(__file__))

def todos_los_paths_del_directorio_y_sus_subdirectorios(directorio):
    return [archivo.as_posix() for archivo in Path(directorio).glob('**/*')]

def obtener_paths_de_archivos():
     return todos_los_paths_del_directorio_y_sus_subdirectorios(obtener_directorio_actual())
     
def _raiz_del_link():
    return "https://www.landinginteligente.com/fotos"

def links_de_archivos(paths_de_archivos):
    dir_final=obtener_directorio_actual().replace('\\','/')
    archivos_final = [path.replace(dir_final, _raiz_del_link()) for path in paths_de_archivos if s.endswith((".txt", ".pdf", ".jpg", ".jpeg", ".png", ".gif"))]
    return archivos_final

def guardar_los_links_en_un_archivo(links):
    with open(obtener_path_del_escritorio(),'Links generados.txt'), "w" as outfile:
        outfile.writelines("\n".join(str(link) for link in links) + '\n')

archivos = obtener_paths_de_archivos(links_de_archivos())
links = links_de_archivos()
guardar_los_links_en_un_archivo(links)

