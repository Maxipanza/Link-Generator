import os
from pathlib import Path


dir_actual = os.path.dirname(os.path.abspath(__file__))

dir_final=dir_actual.replace('\\','/')

gif_list = [ archivo.as_posix() for archivo in Path(dir_actual).glob('**/imagen-interactiva/*')]
fotoagencia_list = [ archivo.as_posix() for archivo in Path(dir_actual).glob('**/foto-agencia/*')]
color_list = [ archivo.as_posix() for archivo in Path(dir_actual).glob('**/colores/*')]
fichatecnica_list = [ archivo.as_posix() for archivo in Path(dir_actual).glob('**/ficha-tecnica/*')]

link = "https://www.landinginteligente.com/fotos"

gif_final = [s.replace(dir_final, link) for s in gif_list]
fotoagencia_final = [s.replace(dir_final, link) for s in fotoagencia_list]
color_final = [s.replace(dir_final, link) for s in color_list]
fichatecnica_final = [s.replace(dir_final, link) for s in fichatecnica_list]


with open(os.path.join(os.path.expanduser('~'),'Desktop','Links generados.txt'), "w") as outfile:
    outfile.writelines("\n".join(str(item) for item in gif_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in fotoagencia_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in color_final) + '\n')
    outfile.writelines("\n")
    outfile.writelines("\n".join(str(item) for item in fichatecnica_final) + '\n')

